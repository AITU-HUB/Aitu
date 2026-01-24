const authBaseInput = document.getElementById('authBase');
const apiBaseInput = document.getElementById('apiBase');
const saveSettingsBtn = document.getElementById('saveSettings');
const flash = document.getElementById('flash');

const loginEmail = document.getElementById('loginEmail');
const loginPassword = document.getElementById('loginPassword');
const loginBtn = document.getElementById('loginBtn');
const logoutBtn = document.getElementById('logoutBtn');
const tokenStatus = document.getElementById('tokenStatus');

const lostfoundFilter = document.getElementById('lostfoundFilter');
const productFilter = document.getElementById('productFilter');

const lostfoundList = document.getElementById('lostfoundList');
const productList = document.getElementById('productList');
const newsList = document.getElementById('newsList');

const lostfoundForm = document.getElementById('lostfoundForm');
const productForm = document.getElementById('productForm');
const newsForm = document.getElementById('newsForm');

const refreshLostFound = document.getElementById('refreshLostFound');
const refreshProducts = document.getElementById('refreshProducts');
const refreshNews = document.getElementById('refreshNews');

function getSettings() {
  return {
    authBase: localStorage.getItem('authBase') || authBaseInput.value,
    apiBase: localStorage.getItem('apiBase') || apiBaseInput.value,
  };
}

function setFlash(message, isError = false) {
  flash.textContent = message;
  flash.style.color = isError ? '#b42318' : '#1f1c1a';
}

function setToken(token) {
  if (token) {
    localStorage.setItem('accessToken', token);
  } else {
    localStorage.removeItem('accessToken');
  }
  updateTokenStatus();
}

function getToken() {
  return localStorage.getItem('accessToken');
}

function updateTokenStatus() {
  const token = getToken();
  tokenStatus.textContent = token ? 'Token stored' : 'No token';
}

function applySettings() {
  const settings = getSettings();
  authBaseInput.value = settings.authBase;
  apiBaseInput.value = settings.apiBase;
}

async function apiRequest(path, options = {}) {
  const settings = getSettings();
  const headers = options.headers || {};
  const token = getToken();
  if (token) {
    headers.Authorization = `Bearer ${token}`;
  }
  const response = await fetch(`${settings.apiBase}${path}`, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...headers,
    },
  });
  if (!response.ok) {
    const text = await response.text();
    throw new Error(text || `Request failed: ${response.status}`);
  }
  if (response.status === 204) {
    return null;
  }
  return response.json();
}

function renderList(container, items, mapper) {
  container.innerHTML = '';
  if (!items.length) {
    container.innerHTML = '<p class="muted">No items yet.</p>';
    return;
  }
  items.forEach((item) => {
    const card = document.createElement('div');
    card.className = 'list-item';
    card.innerHTML = mapper(item);
    container.appendChild(card);
  });
}

async function loadLostFound() {
  const status = lostfoundFilter.value;
  const query = status ? `?status=${status}` : '';
  const items = await apiRequest(`/api/lostfound${query}`);
  renderList(lostfoundList, items, (item) => (
    `<h4>${item.title}</h4>
     <p>Status: ${item.status}</p>
     <p>${item.description}</p>
     <p>Location: ${item.location}</p>
     <p>Contact: ${item.contact_info}</p>`
  ));
}

async function loadProducts() {
  const category = productFilter.value;
  const query = category ? `?category=${category}` : '';
  const items = await apiRequest(`/api/products${query}`);
  renderList(productList, items, (item) => (
    `<h4>${item.title}</h4>
     <p>Category: ${item.category}</p>
     <p>Price: ${item.price} KZT</p>
     <p>${item.description}</p>
     <p>Contact: ${item.contact_info}</p>`
  ));
}

async function loadNews() {
  const items = await apiRequest('/api/news');
  renderList(newsList, items, (item) => (
    `<h4>${item.title}</h4>
     <p>${item.preview_text}</p>
     <p>${item.content}</p>`
  ));
}

async function handleLogin() {
  const settings = getSettings();
  const response = await fetch(`${settings.authBase}/auth/login/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      email: loginEmail.value,
      password: loginPassword.value,
    }),
  });
  if (!response.ok) {
    throw new Error('Login failed');
  }
  const data = await response.json();
  setToken(data.access);
}

function serializeForm(form) {
  return Object.fromEntries(new FormData(form).entries());
}

async function handleCreate(form, endpoint) {
  const payload = serializeForm(form);
  await apiRequest(endpoint, {
    method: 'POST',
    body: JSON.stringify(payload),
  });
  form.reset();
}

saveSettingsBtn.addEventListener('click', () => {
  localStorage.setItem('authBase', authBaseInput.value);
  localStorage.setItem('apiBase', apiBaseInput.value);
  setFlash('Settings saved.');
});

loginBtn.addEventListener('click', async () => {
  try {
    await handleLogin();
    setFlash('Logged in successfully.');
  } catch (error) {
    setFlash(error.message, true);
  }
});

logoutBtn.addEventListener('click', () => {
  setToken(null);
  setFlash('Logged out.');
});

lostfoundFilter.addEventListener('change', () => {
  loadLostFound().catch((error) => setFlash(error.message, true));
});

productFilter.addEventListener('change', () => {
  loadProducts().catch((error) => setFlash(error.message, true));
});

refreshLostFound.addEventListener('click', () => {
  loadLostFound().catch((error) => setFlash(error.message, true));
});

refreshProducts.addEventListener('click', () => {
  loadProducts().catch((error) => setFlash(error.message, true));
});

refreshNews.addEventListener('click', () => {
  loadNews().catch((error) => setFlash(error.message, true));
});

lostfoundForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  try {
    await handleCreate(lostfoundForm, '/api/lostfound');
    setFlash('Lost & Found item created.');
    await loadLostFound();
  } catch (error) {
    setFlash(error.message, true);
  }
});

productForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  try {
    await handleCreate(productForm, '/api/products');
    setFlash('Product created.');
    await loadProducts();
  } catch (error) {
    setFlash(error.message, true);
  }
});

newsForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  try {
    await handleCreate(newsForm, '/api/news');
    setFlash('News created.');
    await loadNews();
  } catch (error) {
    setFlash(error.message, true);
  }
});

applySettings();
updateTokenStatus();

Promise.all([loadLostFound(), loadProducts(), loadNews()]).catch((error) => {
  setFlash(error.message, true);
});