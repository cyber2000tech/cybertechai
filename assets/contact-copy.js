/* Copying the email address is a fallback for browsers without a configured mail app. */
(() => {
  'use strict';
  const button = document.querySelector('[data-copy-email]');
  if (!button) return;
  const status = document.getElementById('contact-copy-status');
  button.addEventListener('click', async () => {
    const address = button.dataset.copyEmail;
    let success = false;
    try {
      if (navigator.clipboard && window.isSecureContext) {
        await navigator.clipboard.writeText(address);
        success = true;
      } else {
        const helper = document.createElement('textarea');
        helper.value = address;
        helper.setAttribute('readonly', '');
        helper.style.position = 'fixed';
        helper.style.opacity = '0';
        document.body.append(helper);
        helper.select();
        success = document.execCommand('copy');
        helper.remove();
      }
    } catch (_) { success = false; }
    if (status) status.textContent = success ? 'Email address copied.' : 'Please select and copy the email address above.';
    button.textContent = success ? 'Copied!' : 'Copy address';
  });
})();
