import { test, expect } from "@playwright/test";

// Paulo jr terralab

test('Remover um projeto cadastrado com sucesso', async ({ page }) => {

    await test.step('login e acesso à tela de projetos', async () => {
        // Acessa a página oficial de testes da Sauce Labs
        await page.goto('https://www.saucedemo.com/'); 
        
        // Garante que o título inicial está correto antes de prosseguir
        await expect(await page.title()).toBe('Swag Labs'); 

        // Preenche as credenciais usando localizadores específicos
        await page.locator('[data-test="username"]').fill('standard_user');
        await page.locator('[data-test="password"]').fill('secret_sauce');
        await page.locator('[data-test="login-button"]').click();

        // Valida se redirecionou com sucesso para a página de inventário (produtos)
        await expect(await page.url()).toBe('https://www.saucedemo.com/inventory.html'); 
    });

    await test.step('identificação e remoção do projeto', async () => {
        // Encontra o bloco/card do produto
        const projetoCard = page.locator('.inventory_item').filter({ hasText: 'Sauce Labs Backpack' });
        await expect(projetoCard).toBeVisible();

        // PASSO EXTRA: Clica em "Add to cart" primeiro para fazer o botão "Remove" aparecer!
        await page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click();

        // Escuta alertas de confirmação do navegador ("Tem certeza?") e aceita automaticamente se aparecer
        page.on('dialog', async dialog => await dialog.accept());

        // Agora sim o botão "Remove" existe e o Playwright vai conseguir clicar nele!
        await page.locator('[data-test="remove-sauce-labs-backpack"]').click();
    });

    await test.step('verificação do sumiço do projeto', async () => {
        // Valida que o botão mudou de volta para "Add to cart", confirmando que a ação de remoção funcionou
        const botaoAdicionar = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]');
        await expect(botaoAdicionar).toBeVisible();
    });
});