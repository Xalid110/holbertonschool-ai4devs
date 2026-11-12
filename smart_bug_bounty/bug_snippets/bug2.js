async function calculateCartTotal(items, discountCode) {
  let subtotal = 0;

  items.forEach(async (item) => {
    const tax = await fetchTaxRate(item.category);
    subtotal += item.price * item.qty * (1 + tax);
  });

  if (discountCode == "SAVE10") {
    subtotal = subtotal - "10";
  }

  return Number(subtotal.toFixed(2));
}

async function fetchTaxRate(category) {
  return category === "books" ? 0.0 : 0.1;
}

calculateCartTotal([{ price: 25, qty: 2, category: "electronics" }], "SAVE10").then(
  console.log
);
