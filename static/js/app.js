// app.js

// Cette fonction va récupérer les produits via l'API Flask
async function fetchProducts() {
    try {
      // Effectuer une requête GET vers l'API Flask qui renvoie la liste des produits
      const response = await fetch('http://127.0.0.1:5000/products');
      
      // Vérifier si la réponse est correcte
      if (response.ok) {
        // Convertir la réponse JSON
        const products = await response.json();
        
        // Afficher les produits dans le DOM
        displayProducts(products);
      } else {
        console.error('Erreur lors de la récupération des produits');
      }
    } catch (error) {
      console.error('Erreur réseau:', error);
    }
  }
  
  // Cette fonction affiche les produits dans le HTML
  function displayProducts(products) {
    // Sélectionner l'élément HTML où les produits seront affichés
    const productsContainer = document.getElementById('products-container');
    
    // Vider l'élément au cas où il contiendrait déjà des données
    productsContainer.innerHTML = '';
  
    // Parcourir les produits et créer un élément HTML pour chaque produit
    products.forEach(product => {
      const productElement = document.createElement('div');
      productElement.classList.add('product');
  
      // Créer le contenu HTML du produit
      productElement.innerHTML = `
        <h3>${product.name}</h3>
        <p>Prix: $${product.price}</p>
        <p>Stock: ${product.stock}</p>
      `;
  
      // Ajouter chaque produit à l'élément container
      productsContainer.appendChild(productElement);
    });
  }
  
  // Appeler la fonction fetchProducts lorsque la page est prête
  document.addEventListener('DOMContentLoaded', fetchProducts);
  