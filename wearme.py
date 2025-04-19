<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>WearMe Jewelry</title>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600&family=Quicksand&display=swap" rel="stylesheet"/>
  <style>
    body {
      margin: 0;
      font-family: 'Quicksand', sans-serif;
      background-color: #fffafc;
      color: #333;
    }

    header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 20px 40px;
      background-color: #fff;
      box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    header h1 {
      font-family: 'Playfair Display', serif;
      font-size: 32px;
      color: #d6a5c0;
    }

    nav a {
      margin-left: 20px;
      text-decoration: none;
      color: #555;
      font-weight: bold;
    }

    .hero {
      background: url('https://images.unsplash.com/photo-1581090700227-1e8f86f2eb38') no-repeat center center/cover;
      height: 80vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      color: #fff;
      text-align: center;
      position: relative;
    }

    .hero h2 {
      font-family: 'Playfair Display', serif;
      font-size: 48px;
      margin-bottom: 10px;
    }

    .hero p {
      font-size: 18px;
      margin-bottom: 20px;
    }

    .hero button {
      padding: 12px 24px;
      font-size: 16px;
      background-color: #d6a5c0;
      border: none;
      color: white;
      cursor: pointer;
      border-radius: 25px;
    }

    .section {
      padding: 60px 40px;
      text-align: center;
    }

    .collections {
      display: flex;
      justify-content: space-around;
      gap: 30px;
      flex-wrap: wrap;
    }

    .collection-card {
      width: 250px;
      background-color: #fff;
      border-radius: 12px;
      box-shadow: 0 5px 15px rgba(0,0,0,0.05);
      padding: 20px;
    }

    .collection-card img {
      width: 100%;
      border-radius: 10px;
    }

    .collection-card h3 {
      margin-top: 15px;
      color: #d6a5c0;
    }

    footer {
      background-color: #fce4ec;
      text-align: center;
      padding: 30px 20px;
      font-size: 14px;
      color: #555;
    }
  </style>
</head>
<body>

  <header>
    <h1>WearMe</h1>
    <nav>
      <a href="#">Home</a>
      <a href="#">Shop</a>
      <a href="#">About</a>
      <a href="#">Contact</a>
      <a href="#">Cart</a>
    </nav>
  </header>

  <section class="hero">
    <h2>Jewelry That Tells Your Story</h2>
    <p>Handmade elegance for every moment</p>
    <button>Shop Now</button>
  </section>

  <section class="section">
    <h2>Our Collections</h2>
    <div class="collections">
      <div class="collection-card">
        <img src="https://images.unsplash.com/photo-1589478584005-c8cddf06038e" alt="Necklaces">
        <h3>Necklaces</h3>
      </div>
      <div class="collection-card">
        <img src="https://images.unsplash.com/photo-1581092913115-bc52dc5c8d03" alt="Rings">
        <h3>Rings</h3>
      </div>
      <div class="collection-card">
        <img src="https://images.unsplash.com/photo-1618354691213-d20e4b10504a" alt="Earrings">
        <h3>Earrings</h3>
      </div>
    </div>
  </section>

  <footer>
    &copy; 2025 WearMe Jewelry — All Rights Reserved
  </footer>

</body>
</html>