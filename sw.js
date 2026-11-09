self.addEventListener('install', (e) => { self.skipWaiting(); });
self.addEventListener('fetch', (event) => {
  // We only look at files coming from your github pages
  if (event.request.url.includes('onyxsoul-1.github.io')) {
    event.respondWith(
      fetch(event.request).then((response) => {
        const newHeaders = new Headers(response.headers);
        // THE MAGIC HEADERS THAT STOP THE ERROR
        newHeaders.set('Cross-Origin-Opener-Policy', 'same-origin');
        newHeaders.set('Cross-Origin-Embedder-Policy', 'require-corp');
        return new Response(response.body, {
          status: response.status,
          statusText: response.statusText,
          headers: newHeaders
        });
      })
    );
  }
});
