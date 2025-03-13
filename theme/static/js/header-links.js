document.addEventListener('DOMContentLoaded', function() {
  // Find all headers within .content
  const headers = document.querySelectorAll('.content h1[id], .content h2[id], .content h3[id], .content h4[id], .content h5[id], .content h6[id]');

  headers.forEach(function(header) {
    // Create the anchor element
    const anchor = document.createElement('a');
    anchor.className = 'header-link';
    anchor.innerHTML = '#';
    anchor.href = '#' + header.id;
    anchor.title = 'Permalink to this section';

    // Append the anchor to the header
    header.appendChild(anchor);
  });
});
