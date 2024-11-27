// Fonction pour récupérer les produits (GET)
function getProducts() {
    fetch('/products')
        .then(response => response.json())
        .then(data => {
            const productList = document.getElementById('product-list');
            productList.innerHTML = ''; // Vider la liste avant de la remplir
            data.forEach(product => {
                const listItem = document.createElement('li');
                listItem.textContent = `${product.name} - Prix: ${product.price}€ - Stock: ${product.stock}`;
                productList.appendChild(listItem);
            });
        })
        .catch(error => console.error('Error fetching products:', error));
}

// Fonction pour ajouter un produit (POST)
document.getElementById('add-product-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById('product-name').value;
    const price = document.getElementById('product-price').value;
    const stock = document.getElementById('product-stock').value;

    const productData = {
        name: name,
        price: parseFloat(price), // Assurez-vous que le prix est un nombre flottant
        stock: parseInt(stock)    // Assurez-vous que le stock est un nombre entier
    };

    fetch('/products', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(productData)
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);  // Afficher le message de succès
        getProducts();  // Mettre à jour la liste des produits après ajout
    })
    .catch(error => console.error('Error adding product:', error));
});

// Initialiser l'affichage des produits au chargement de la page
getProducts();
