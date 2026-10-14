# V34 Contact Reliability Fix

## Root cause
The old “Start a conversation” link was `mailto:`. This delegates to the visitor’s locally configured mail handler. It neither submits a message from the website nor guarantees Gmail opens. On some browsers/iPhones, a permission prompt appears but no draft opens if a mail handler is missing or misconfigured.

## Website changes
- Replace the primary contact action with **Open Gmail** using an HTTPS Gmail compose URL containing the correct recipient, a subject and an optional draft message.
- Keep **Use another email app** with `mailto:` for Outlook, Apple Mail and other mail apps.
- Add a **Copy address** button with secure clipboard and fallback copying plus accessible status feedback.
- State clearly that visitors must press **Send** in their own email service.
- Small CSS polish of the contact card, responsive from narrow phones to desktops. All approved technical content and other pages are unchanged.

## Important testing limitation
This static GitHub Pages website has no email-delivery backend. The buttons can create drafts or copy an address, but the website **cannot verify whether an email was actually sent or delivered**. Check using a personal account and confirm arrival in `cyber2000tech@gmail.com` Inbox and Spam. A genuine website-native “Send Message” form would need an email service/backend and its configuration.

## Publishing
Upload the files from this ZIP to the GitHub Pages repository, retaining the `assets/` directory and `CNAME`. The live website is not automatically changed by generating this package.
