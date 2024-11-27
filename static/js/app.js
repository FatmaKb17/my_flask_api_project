document.addEventListener('DOMContentLoaded', () => {
    fetch('/products')
        .then(response => response.json())
        .then(data => {
            const productList = document.getElementById('product-list');
            data.forEach(product => {
                const li = document.createElement('li');
                li.textContent = `${product.name} - ${product.price}€ (Stock: ${product.stock})`;
                productList.appendChild(li);
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});
