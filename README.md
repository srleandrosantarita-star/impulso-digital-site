# Soluções da Internet

Landing page da Soluções da Internet — sites, aplicativos inteligentes, automação de processos e suporte técnico.

## Stack

HTML, CSS e JavaScript puros, sem build step.

## Estrutura

```
index.html          Página principal
privacidade.html     Política de Privacidade
termos.html          Termos de Uso
assets/css/          Estilos
assets/js/           Interações e animações
assets/img/          Logo
assets/audio/        Música de fundo
```

## Deploy

Publicado no GitHub Pages a partir do branch `master`. Domínio próprio planejado: `solucoesdainternet.com.br` (ver arquivo `CNAME`) — assim que o registro em registro.br estiver ativo, aponte o DNS conforme abaixo:

- **Apex (`solucoesdainternet.com.br`)**: registros A para `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
- **`www`**: registro CNAME para `srleandrosantarita-star.github.io`

Depois de configurar o DNS, ative "Enforce HTTPS" nas configurações de Pages do repositório.
