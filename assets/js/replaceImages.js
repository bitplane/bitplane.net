// /assets/js/replaceImages.js

/**
 * Replace images whose alt attribute starts with `prefix:` by calling `callback(fileName, img)`.
 * The `callback` should return a DOM element to replace the image.
 * If the image is inside a link, the image is removed from the link and
 * the returned DOM element is inserted after the link.
 *
 * @param {string} prefix - The prefix, e.g. "amiga".
 * @param {function(string, HTMLImageElement): HTMLElement} callback - Takes the file name and the img element, returns a DOM element.
 */
export function replaceImages(prefix, callback) {
  const images = document.querySelectorAll(`img[alt^="${prefix}:"]`);
  for (const img of images) {
    const alt = img.getAttribute("alt");
    const fileName = alt.substring(prefix.length + 1);
    const replacement = callback(fileName, img);

    if (!(replacement instanceof HTMLElement)) {
      console.error("callback did not return a DOM element");
      continue;
    }

    const parent = img.parentNode;
    if (parent && parent.tagName === 'A') {
      // If inside a link, remove the image and insert the emulator after the link
      parent.removeChild(img);
      parent.parentNode.insertBefore(replacement, parent.nextSibling);
    } else {
      // Normal replacement if not inside a link
      img.parentNode.replaceChild(replacement, img);
    }
  }
}

