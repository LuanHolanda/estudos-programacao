# 📋 Tabelas em HTML

As tabelas em HTML são utilizadas para organizar informações em linhas e colunas.

Principais tags:
- `<table>` → define a tabela inteira
- `<tr>` → cria uma linha
- `<th>` → cria o cabeçalho da tabela
- `<td>` → cria os dados/células da tabela

Exemplo:

```html
<table border="1">

  <tr>
    <th>Nome</th>
    <th>Idade</th>
  </tr>

  <tr>
    <td>Luan</td>
    <td>24</td>
  </tr>

  <tr>
    <td>Maria</td>
    <td>22</td>
  </tr>

</table>
```

Estrutura visual:

```text
<table>
 ├── <tr>
 │     ├── <th>
 │     └── <th>
 │
 ├── <tr>
 │     ├── <td>
 │     └── <td>
```

# 🔗 Links em HTML

A tag `<a>` é utilizada para criar links em páginas HTML.

## Exemplo

```html
<a href="https://google.com">Acessar Google</a>
```

## Principais atributos
- `href` → define o destino do link
- `target="_blank"` → abre o link em outra aba

## Exemplo

```html
<a href="https://google.com" target="_blank">
  Abrir Google
</a>
```

---



# 🖼️ Imagens em HTML

A tag `<img>` é utilizada para inserir imagens na página.

## Exemplo

```html
<img src="imagem.jpg" alt="Descrição da imagem">
```

## Principais atributos
- `src` → caminho da imagem
- `alt` → descrição da imagem
- `width` → largura
- `height` → altura

## Exemplo

```html
<img src="foto.png" alt="Foto de perfil" width="200">
```

---

# 📝 Formulários em HTML

A tag `<form>` é utilizada para criar formulários e receber dados do usuário.

## Principais tags

### `<form>`
Cria o formulário.

### `<input>`
Campo de entrada de dados.

### `<label>`
Texto descritivo do campo.

### `<button>`
Botão do formulário.

---

## Exemplo

```html
<form>

  <label>Nome:</label>
  <input type="text">

  <label>Senha:</label>
  <input type="password">

  <button type="submit">
    Enviar
  </button>

</form>
```

## Tipos de input
- `text`
- `password`
- `email`
- `number`
- `checkbox`
- `radio`
- `file`