class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.items = page.locator(".inventory_item")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_to_cart(self, product_name):
        item = self.items.filter(has_text=product_name)
        item.get_by_role("button", name="Add to cart").click()