// Contact form handler for 100creatives.com
//
// Delivery is via Resend. Set these environment variables in the Vercel
// project (Settings -> Environment Variables):
//
//   RESEND_API_KEY  - required. API key from resend.com
//   CONTACT_TO      - optional. Defaults to abhi@paperkites.co
//   CONTACT_FROM    - optional. Defaults to forms@100creatives.com
//                     The sending domain must be verified in Resend.
//
// Without RESEND_API_KEY the endpoint returns 503 and the browser falls back
// to opening a pre-filled email, so a submission is never silently dropped.

const TO = process.env.CONTACT_TO || 'abhi@paperkites.co';
const FROM = process.env.CONTACT_FROM || 'forms@100creatives.com';

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const body = typeof req.body === 'string' ? JSON.parse(req.body || '{}') : (req.body || {});
  const { name, email, company, service, budget, message, website } = body;

  // Honeypot: real users never fill this hidden field.
  if (website) return res.status(200).json({ ok: true });

  if (!name || !email || !message) {
    return res.status(400).json({ error: 'Name, email, and project details are required.' });
  }

  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    return res.status(400).json({ error: 'Please enter a valid email address.' });
  }

  if (String(message).length > 5000) {
    return res.status(400).json({ error: 'Message is too long.' });
  }

  if (!process.env.RESEND_API_KEY) {
    return res.status(503).json({ error: 'Form delivery is not configured.' });
  }

  const rows = [
    ['Name', name],
    ['Email', email],
    ['Company', company || '—'],
    ['Service', service || '—'],
    ['Budget', budget || '—'],
  ]
    .map(([k, v]) => `<tr><td style="padding:4px 12px 4px 0;color:#777;">${k}</td><td style="padding:4px 0;"><strong>${escapeHtml(v)}</strong></td></tr>`)
    .join('');

  try {
    const response = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${process.env.RESEND_API_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        from: `100 Creatives <${FROM}>`,
        to: [TO],
        reply_to: email,
        subject: `New enquiry — ${name}${company ? ` (${company})` : ''}`,
        html: `
          <h2 style="font-family:Georgia,serif;font-weight:400;">New enquiry from 100creatives.com</h2>
          <table style="font-family:system-ui,sans-serif;font-size:14px;border-collapse:collapse;">${rows}</table>
          <p style="font-family:system-ui,sans-serif;font-size:14px;color:#777;margin-top:24px;">Project details</p>
          <p style="font-family:system-ui,sans-serif;font-size:15px;line-height:1.7;white-space:pre-wrap;">${escapeHtml(message)}</p>
        `,
      }),
    });

    if (!response.ok) {
      const detail = await response.text();
      console.error('Resend error:', response.status, detail);
      return res.status(502).json({ error: 'Could not send your message.' });
    }

    return res.status(200).json({ ok: true });
  } catch (err) {
    console.error('Contact form error:', err);
    return res.status(502).json({ error: 'Could not send your message.' });
  }
}
