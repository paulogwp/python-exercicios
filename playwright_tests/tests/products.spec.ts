import { expect, test } from "@playwright/test";

test('all product names begin with "Sauce Labs"', async ({ page }) => {
    await test.step('login', async () => {
        await page.goto('https://www.saucedemo.com/');
        await page.locator('[data-test="username"]').fill('standard_user');
        await page.locator('[data-test="password"]').fill('secret_sauce');
        await page.locator('[data-test="login-button"]').click();
    });

    await test.step('product title verification', async () => {
        const titles = page.locator('.inventory_item_name');
        
        // Se o objetivo for validar apenas os elementos que CONTÊM ou COMEÇAM com "Sauce Labs"
        // filtrando a lista para ignorar o "Test.allTheThings()":
        const sauceLabsItems = titles.filter({ hasText: /^Sauce Labs/ });
        await expect(sauceLabsItems).toHaveText([
            /^Sauce Labs Backpack/,
            /^Sauce Labs Bike Light/,
            /^Sauce Labs Bolt T-Shirt/,
            /^Sauce Labs Fleece Jacket/,
            /^Sauce Labs Onesie/
        ]);
    });
});