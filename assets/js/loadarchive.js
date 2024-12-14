// Assumes `fetch` and `JSZip` are available

export async function loadArchive(url, filterFn) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`Failed to fetch ${url}: ${res.statusText}`);

  const buf = await res.arrayBuffer();
  const zip = await JSZip.loadAsync(buf);

  const entries = [];
  zip.forEach((relativePath, zipEntry) => {
    if (!zipEntry.dir && filterFn(zipEntry.name)) {
      entries.push(zipEntry.async("arraybuffer").then(data => ({
        name: zipEntry.name,
        data
      })));
    }
  });

  return Promise.all(entries);
}

