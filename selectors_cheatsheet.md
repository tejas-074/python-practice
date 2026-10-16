# Selector cheat sheet

| # | Element | Page | CSS | XPath |
|---|---|---|---|---|
| 1 | Username box | saucedemo login | `[data-test="username"]` | `//input[@data-test="username"]` |
| 2 | Password box | saucedemo login | `[data-test="password"]` | `//input[@data-test="password"]` |
| 3 | Login button | saucedemo login | `#login-button` | `//input[@id="login-button"]` |
| 4 | Page title | saucedemo products | `[data-test="title"]` | `//span[@data-test="title"]` |
| 5 | Cart link | saucedemo products | `[data-test="shopping-cart-link"]` | `//a[@data-test="shopping-cart-link"]` |
| 6 | Add to cart, Backpack | saucedemo products | `[data-test="add-to-cart-sauce-labs-backpack"]` | `//button[@data-test="add-to-cart-sauce-labs-backpack"]` |
| 7 | Menu button | saucedemo products | `#react-burger-menu-btn` | `//button[@id="react-burger-menu-btn"]` |
| 8 | Sort dropdown | saucedemo products | `[data-test="product-sort-container"]` | `//select[@data-test="product-sort-container"]` |
| 9 | Backpack name | saucedemo products | `#item_4_title_link` | `//div[text()="Sauce Labs Backpack"]` |
| 10 | Username box | the-internet login | `#username` | `//input[@id="username"]` |
| 11 | Password box | the-internet login | `#password` | `//input[@id="password"]` |
| 12 | Login button | the-internet login | `button[type="submit"]` | `//button[@type="submit"]` |
| 13 | Dropdown | the-internet dropdown | `#dropdown` | `//select[@id="dropdown"]` |
| 14 | Number box | the-internet inputs | `input[type="number"]` | `//input[@type="number"]` |
| 15 | Add Element button | the-internet add/remove | `button[onclick="addElement()"]` | `//button[@onclick="addElement()"]` |
| 16 | First checkbox | the-internet checkboxes | `#checkboxes input:nth-of-type(1)` | `(//input[@type="checkbox"])[1]` |
| 17 | Second checkbox | the-internet checkboxes | `#checkboxes input:nth-of-type(2)` | `(//input[@type="checkbox"])[2]` |
| 18 | Table 1 | the-internet tables | `#table1` | `//table[@id="table1"]` |
| 19 | Edit link, Smith row | the-internet tables | `#table1 tbody tr:nth-child(1) a[href="#edit"]` | `//table[@id="table1"]//td[text()="Smith"]/..//a[text()="edit"]` |
| 20 | Login error message | the-internet login | `#flash` | `//div[@id="flash"]` |