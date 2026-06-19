const { Builder, By, until } = require('selenium-webdriver');

async function executarTeste(nomeTeste, endereco) {

    let driver = await new Builder()
        .forBrowser('chrome')
        .build();

    try {

        console.log(`\n=== ${nomeTeste} ===`);

        await driver.get('https://www.terraplanner.org');
        await driver.manage().window().maximize();

        const campo = await driver.wait(
            until.elementLocated(By.name('search')),
            15000
        );

        await campo.click();

        if (endereco !== null) {
            await campo.sendKeys(endereco);
            console.log(`Texto digitado: ${endereco}`);
        }

        const botao = await driver.wait(
            until.elementLocated(
                By.css('button[data-testid="button-search-input-field-search"]')
            ),
            10000
        );

        await botao.click();

        console.log("Botão clicado");

        // Tempo para observar o resultado
        await driver.sleep(5000);

        console.log(`${nomeTeste} concluído com sucesso.`);

    } catch (erro) {

        console.error(`Erro no teste: ${nomeTeste}`);
        console.error(erro);

    } finally {

        await driver.quit();

    }
}

async function executarTodosOsTestes() {

    // TESTE 1 - Endereço válido
    await executarTeste(
        "TESTE 1 - Endereço válido",
        "Praça Tiradentes, MG Ouro Preto"
    );

    // TESTE 2 - Endereço inexistente
    await executarTeste(
        "TESTE 2 - Endereço inexistente",
        "Rua Inexistente 999 Cidade Fantasma"
    );

    // TESTE 3 - Campo vazio
    await executarTeste(
        "TESTE 3 - Pesquisa vazia",
        null
    );

    console.log("\nTodos os testes finalizaram.");
}

executarTodosOsTestes();