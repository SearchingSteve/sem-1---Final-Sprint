// Description: JS file for processing objects from gameinventory.json

// Author: Stephen Crocker
// Date - Apr 4, 2024

// Set constants for program if needed
totalValue = 0
totalProfit = 0

// FETCH and READ the people.json disk file
fetch('./gameinventory.json')
  .then(response => response.json())
  .then(data => {
    // Create a container to hold the game inventory data
    const container = document.createElement('div');
    container.id = 'gameInventoryContainer';

    // Iterate through each game in the JSON file
    data.forEach(game => {
      // Create new div for each game
      const gameDiv = document.createElement('div');
      gameDiv.className = 'game';

      // Perform calculations each iteration to update totalProfit 
      totalProfit += getProfit(game);


      // Add the game's data to the div
      gameDiv.innerHTML = `
        <h2>Item Name: ${getItemName(game)}</h2>
        <p>Item Category: ${getItemCategory(game)}</p>
        <p>Net Income: ${getConsoleType(game)}</p>
        <p>Quantity: ${getQuantity(game)}</p>
        <p>Price Paid: ${getPricePaid(game)}</p>
        <p>Market Value: ${getItemPrice(game)}</p>
        <p>Condition: ${getCondition(game)}</p>
        <p>Profit: ${getProfit(game)}</p>
        <br><br>
      `;

      // Add the game's div to the container
      container.appendChild(gameDiv);

      // Also log the data to the console
      console.log(getItemName(game));
      console.log(getItemCategory(game));
      console.log(getConsoleType(game));
      console.log(getQuantity(game));
      console.log(getPricePaid(game));
      console.log(getItemPrice(game));
      console.log(getCondition(game));
      console.log(getProfit(game));
    });


     // Create a new div to display total profit - outside for loop
    const totalProfitDiv = document.createElement('div');
    totalProfitDiv.innerHTML = `<h3>Total Profit: ${totalProfit}</h3>`;
 
     // Add the total profit div to the container
    container.appendChild(totalProfitDiv);
 
    // Add the container to the body of the HTML
    document.body.appendChild(container);
  })
  .catch(error => {
    // Handle any errors that occur while fetching the file
    console.error(error);
  });

  

  function getItemName(game) {
    return game.itemName
} 

  function getItemCategory(game) {    
    return game.itemCategory
  }

  function getConsoleType(game){
    return game.consoleType
  }

  function getQuantity(game){
    return game.quantity
  }

  function getPricePaid(game){
    return `$${game.pricePaid}`
  }

  function getItemPrice(game){
    return `$${game.itemPrice}`
  }

  function getCondition(game){
    return game.condition
  }

  function getProfit(game){
    return (game.itemPrice - game.pricePaid)
  }

  console.log(html);
  document.body.innerHTML = html;
  