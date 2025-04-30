describe('Cadastro, login e compra', () => {
    const uuid = Date.now(); // Garante nome de usuário único
    const username = `usuario${uuid}`;
    const password = 'Senha123@';
  
    it('deve cadastrar um novo usuário, logar, adicionar produto e finalizar compra', () => {
      // 1. Acessar página de cadastro
      cy.visit('http://localhost:8000/register/');
  
      // 2. Preencher o formulário de cadastro
      cy.get('input[name="username"]').type(username);
      cy.get('input[name="email"]').type(`${username}@teste.com`);
      cy.get('input[name="password1"]').type(password);
      cy.get('input[name="password2"]').type(password);
  
      // 3. Submeter cadastro
      cy.get('form').submit();
  
      // 4. Verificar redirecionamento para home
      cy.url().should('include', '/');
      cy.get('h1').should('contain.text', 'Bem-vindo ao Mercado!');
  
      // 5. Adicionar o primeiro produto ao carrinho
      cy.get('form[action*="carrinho/adicionar"]').first().within(() => {
        cy.get('button[type="submit"]').click();
      });
  
      // 6. Ir para o carrinho
      cy.visit('http://localhost:8000/carrinho/');
  
      // 7. Finalizar compra
      cy.get('form[action*="finalizar"]').submit();
  
      // 8. Confirmar página de sucesso
      cy.url().should('include', '/compra/sucesso');
      cy.contains('Compra Realizada com Sucesso');
    });
  });
  