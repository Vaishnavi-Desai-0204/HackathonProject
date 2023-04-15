// Get references to the conveyer container and all the items
var container = document.querySelector('.conveyer-container');
var items = document.querySelectorAll('.outfit');

// Add event listeners to the container for scroll events
container.addEventListener('scroll', function() {
    // Loop through all the items and calculate their distance from the center of the container
    for (var i = 0; i < items.length; i++) {
        var item = items[i];
        var itemRect = item.getBoundingClientRect();
        var containerRect = container.getBoundingClientRect();
        var center = containerRect.left + containerRect.width / 2;
        var distance = Math.abs(itemRect.left + itemRect.width / 2 - center);

        // If the item is within a certain distance from the center, add the 'selected' class to it
        if (distance < itemRect.width / 2) {
            item.classList.add('selected');
        } else {
            item.classList.remove('selected');
        }
    }
});
