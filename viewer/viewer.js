// Minimal manifest-driven viewer script
const manifestPath = '/Nomimi/assets/manifest.json'; // adjust if hosted at a different root
const assetSelect = document.getElementById('assetSelect');
const viewer = document.getElementById('viewer');
const meta = document.getElementById('meta');

async function loadManifest() {
  try {
    const res = await fetch(manifestPath);
    if (!res.ok) throw new Error('Failed to load manifest: ' + res.status);
    const manifest = await res.json();
    populate(manifest.assets || []);
  } catch (err) {
    assetSelect.innerHTML = '<option>Error loading manifest</option>';
    meta.textContent = err.message;
    console.error(err);
  }
}

function populate(assets) {
  assetSelect.innerHTML = '';
  assets.forEach((a, i) => {
    const opt = document.createElement('option');
    opt.value = a.path;
    opt.textContent = `${a.name || a.id} — ${a.tags ? a.tags.join(',') : ''}`;
    opt.dataset.meta = JSON.stringify(a);
    assetSelect.appendChild(opt);
  });
  assetSelect.addEventListener('change', () => {
    const selected = assetSelect.selectedOptions[0];
    if (!selected) return;
    const metaObj = JSON.parse(selected.dataset.meta || '{}');
    viewer.setAttribute('src', selected.value);
    meta.innerHTML = `<strong>${metaObj.name || ''}</strong><br/>ID: ${metaObj.id || ''}<br/>Tags: ${metaObj.tags ? metaObj.tags.join(', ') : '—'}`;
  });
  if (assets.length) {
    assetSelect.selectedIndex = 0;
    assetSelect.dispatchEvent(new Event('change'));
  }
}

loadManifest();