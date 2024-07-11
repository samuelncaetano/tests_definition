# Testes Unitários

## Princípios de Design

1. **First (Rápido, Independente, Repetível, Auto-Verificável, e Temporal)**:

   - **Rápido (Fast)**: Testes devem ser rápidos para não desencorajar a execução frequente.
   - **Independente (Independent)**: Testes não devem depender uns dos outros.
   - **Repetível (Repeatable)**: Testes devem dar os mesmos resultados em qualquer ambiente.
   - **Auto-Verificável (Self-Validating)**: Testes devem ser binários (passar ou falhar).
   - **Temporal (Timely)**: Testes devem ser escritos logo após a implementação do código.

2. **KISS (Keep It Simple, Stupid)**:

   - Mantenha os testes simples e focados em um único comportamento ou funcionalidade por teste.

3. **DRY (Don't Repeat Yourself)**:

   - Evite duplicação de código nos testes. Use métodos de configuração e teardown adequados.

4. **SOLID**:
   - **Single Responsibility Principle (SRP)**: Um teste deve testar uma única funcionalidade.
   - **Open/Closed Principle (OCP)**: Os testes devem ser escritos de forma que possam ser facilmente estendidos para novas funcionalidades.
   - **Liskov Substitution Principle (LSP)**: Mantenha a consistência no uso de objetos substituíveis em testes.
   - **Interface Segregation Principle (ISP)**: Utilize interfaces específicas para o que está sendo testado.
   - **Dependency Inversion Principle (DIP)**: Utilize injeção de dependências para facilitar o isolamento de unidades a serem testadas.

## Padrões de Design

1. **Arrange-Act-Assert (AAA)**:

   - **Arrange**: Configure o contexto do teste.
   - **Act**: Execute a ação ou comportamento que está sendo testado.
   - **Assert**: Verifique se o resultado esperado ocorreu.

2. **Test Data Builders**:

   - Use builders para criar objetos complexos de maneira fácil e reutilizável.

3. **Mock Objects**:

   - Utilize mocks para simular comportamentos de dependências externas.

4. **Parameterized Tests**:
   - Use testes parametrizados para testar múltiplos cenários com diferentes conjuntos de dados.

## Boas Práticas

- **Nomes Descritivos**: Nomeie os testes de maneira que descrevam claramente o que está sendo testado.
- **Feedback Rápido**: Estruture os testes para fornecer feedback rápido sobre falhas.
- **Cobertura de Código**: Almeje alta cobertura de código, mas não em detrimento da qualidade dos testes.
- **Isolamento de Testes**: Certifique-se de que os testes não dependam do estado deixado por outros testes.
