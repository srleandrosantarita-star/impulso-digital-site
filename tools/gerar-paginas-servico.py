# -*- coding: utf-8 -*-
"""
Gera as cinco páginas de serviço a partir do conteúdo definido em PAGES.

    python tools/gerar-paginas-servico.py

Os arquivos são sempre escritos na raiz do repositório, independente do
diretório de onde o script for chamado. Os arquivos gerados SÃO versionados —
o script existe para manter as cinco páginas consistentes entre si, não para
substituí-las no deploy (o GitHub Pages serve o HTML direto, sem build).

Para alterar o conteúdo de uma página, edite PAGES e rode o script de novo.
Editar o HTML na mão funciona, mas a próxima execução sobrescreve a alteração.

Atenção: o texto das FAQs aparece duas vezes em cada página — no HTML visível
e no JSON-LD que os buscadores leem. O script cuida de manter os dois iguais;
uma edição manual no HTML desalinha essa dupla sem aviso.
"""
import io, json, os

BASE = "https://solucoesdainternet.com.br/"
CSSV = "1789057368"

PAGES = [
{
 "slug":"criacao-de-sites-balneario-camboriu.html",
 "nav":"Criação de Sites",
 "h1":"Criação de Sites em Balneário Camboriú",
 "title":"Criação de Sites em Balneário Camboriú/SC — Soluções da Internet",
 "desc":"Criação de sites profissionais em Balneário Camboriú: sites institucionais, landing pages e lojas virtuais rápidos, responsivos e otimizados para aparecer no Google.",
 "sub":"Sites institucionais, landing pages e lojas virtuais feitos sob medida — rápidos, responsivos e preparados para aparecer no Google e transformar visitantes em clientes.",
 "svc_name":"Criação de Sites",
 "cities":["Balneário Camboriú","Camboriú"],
 "intro":[
   "Um site que demora para carregar, não funciona bem no celular ou não aparece no Google é dinheiro parado. A <strong>Soluções da Internet</strong> desenvolve sites em <strong>Balneário Camboriú</strong> pensados em três coisas: velocidade, aparência profissional e conversão — ou seja, transformar quem visita em quem entra em contato.",
   "Atendemos presencialmente <strong>Balneário Camboriú e Camboriú</strong> e, como todo o processo pode ser feito à distância, trabalhamos também com clientes de outras cidades e estados."
 ],
 "incl_title":"O que está incluído",
 "incl":[
   "<strong>Design exclusivo</strong> — nada de template genérico: o layout é construído a partir da identidade do seu negócio.",
   "<strong>100% responsivo</strong> — funciona igualmente bem no celular, tablet e computador, onde a maioria dos seus clientes vai acessar.",
   "<strong>Otimizado para o Google (SEO)</strong> — estrutura, títulos, velocidade e dados estruturados configurados desde o primeiro dia.",
   "<strong>Velocidade de carregamento</strong> — páginas leves, porque cada segundo a mais de carregamento derruba a taxa de conversão.",
   "<strong>Integração com WhatsApp</strong> — o cliente fala com você em um clique, sem formulário complicado.",
   "<strong>Certificado de segurança (HTTPS)</strong> e hospedagem configurada, já inclusos.",
   "<strong>Treinamento e suporte</strong> — você aprende a mexer no que precisa, e continuamos por perto depois da entrega."
 ],
 "steps_title":"Como funciona o processo",
 "steps":[
   ("Diagnóstico","Conversamos sobre o seu negócio, seus clientes e o que o site precisa resolver. Sem jargão técnico."),
   ("Proposta","Você recebe escopo, prazo e valor fechado por escrito. Sem surpresa no meio do caminho."),
   ("Desenvolvimento","Construímos o site e você acompanha o andamento, com espaço para ajustes."),
   ("Entrega e suporte","Publicamos o site no ar, configuramos o Google e seguimos dando suporte.")
 ],
 "faq":[
   ("Quanto custa um site em Balneário Camboriú?","O valor depende do tamanho e da complexidade: uma landing page de uma página tem um custo bem diferente de um site institucional com várias seções ou de uma loja virtual. Fazemos um orçamento gratuito e sem compromisso depois de entender o que você precisa — e o valor é fechado antes de começar."),
   ("Quanto tempo leva para ficar pronto?","Na maioria dos casos, de 1 a 3 semanas — uma landing page fica pronta mais perto de uma semana, e um site institucional maior se aproxima de três. O que mais influencia o prazo não é o nosso trabalho, e sim a agilidade na aprovação dos textos e imagens. O prazo do seu caso é fechado por escrito junto com o escopo, antes de começarmos."),
   ("Preciso ter logo, textos e fotos prontos?","Ajuda bastante, mas não é obrigatório. Se você não tiver o material pronto, orientamos sobre o que é necessário e ajudamos a estruturar os textos e escolher imagens adequadas."),
   ("O site vai aparecer no Google?","Entregamos o site tecnicamente preparado para o Google: estrutura correta, velocidade, dados estruturados e cadastro no Search Console. Aparecer nas primeiras posições depende também da concorrência do seu segmento e de um trabalho contínuo — e é justamente isso que explicamos com honestidade na proposta, sem prometer primeiro lugar."),
   ("Vocês atendem fora de Balneário Camboriú?","Sim. O atendimento presencial é em Balneário Camboriú e Camboriú, mas a criação de um site é feita integralmente à distância — reuniões, aprovações e entrega — então atendemos clientes de qualquer cidade do Brasil sem prejuízo nenhum no resultado.")
 ]
},
{
 "slug":"recuperacao-de-dados-balneario-camboriu.html",
 "nav":"Recuperação de Dados",
 "h1":"Recuperação de Dados e Arquivos em Balneário Camboriú",
 "title":"Recuperação de Dados e Arquivos em Balneário Camboriú/SC — Soluções da Internet",
 "desc":"Recuperação de arquivos perdidos em HD, SSD, pen drive e cartão de memória em Balneário Camboriú e Camboriú. Diagnóstico gratuito antes do orçamento.",
 "sub":"Arquivos apagados, HD que não liga, pen drive que o computador não reconhece. O diagnóstico é gratuito: explicamos o que dá — e o que não dá — para recuperar antes de você pagar qualquer coisa.",
 "svc_name":"Recuperação de Arquivos e Dados",
 "cities":["Balneário Camboriú","Camboriú"],
 "intro":[
   "Perder arquivos é sempre urgente: a contabilidade da empresa, as fotos de anos, o projeto que estava quase pronto. A <strong>Soluções da Internet</strong> trabalha com recuperação de dados em <strong>Balneário Camboriú e Camboriú</strong>, em HDs, SSDs, pen drives e cartões de memória.",
   "A primeira coisa que fazemos é o <strong>diagnóstico gratuito</strong>: analisamos a mídia e dizemos com clareza o que é possível recuperar e qual o custo. Você só paga se autorizar o serviço depois disso."
 ],
 "incl_title":"Casos que atendemos",
 "incl":[
   "<strong>Arquivos apagados por engano</strong> — exclusão acidental, lixeira esvaziada, formatação rápida.",
   "<strong>HD ou SSD que não é reconhecido</strong> pelo computador, ou que aparece pedindo formatação.",
   "<strong>Pen drive e cartão de memória</strong> corrompidos ou ilegíveis.",
   "<strong>Partição perdida ou corrompida</strong> após atualização, queda de energia ou erro de sistema.",
   "<strong>Sistema que não inicia</strong> — recuperamos os dados mesmo quando o Windows não abre mais.",
   "<strong>Backup do que sobrou</strong> — devolvemos os arquivos organizados em uma mídia segura."
 ],
 "steps_title":"Como funciona",
 "steps":[
   ("Pare de usar a mídia","Continuar usando o disco onde os arquivos sumiram é o que mais reduz a chance de recuperação. Desligue e nos chame."),
   ("Diagnóstico gratuito","Analisamos a mídia e identificamos o que é recuperável e qual a causa do problema, sem custo."),
   ("Orçamento","Você recebe o valor e a lista do que conseguimos recuperar antes de autorizar o serviço."),
   ("Entrega","Devolvemos os arquivos em mídia segura e orientamos sobre backup para não acontecer de novo.")
 ],
 "faq":[
   ("O diagnóstico é cobrado?","Não. O diagnóstico é gratuito: analisamos a mídia, dizemos o que é recuperável e apresentamos o orçamento. Você decide a partir daí, sem ter gasto nada até esse ponto."),
   ("Dá para recuperar qualquer arquivo?","Não. Há casos em que a mídia sofreu dano físico severo ou os dados foram sobrescritos, e nesses casos a recuperação não é possível. Por isso o diagnóstico vem primeiro e somos francos sobre as chances — inclusive quando a resposta é que não há o que fazer."),
   ("Quanto custa a recuperação de dados?","O valor depende do tipo de mídia e da complexidade do caso — uma exclusão acidental é bem mais simples que um disco com dano físico. Como o diagnóstico é gratuito, você recebe o valor exato do seu caso antes de decidir."),
   ("Quanto tempo demora?","Varia muito conforme a causa do problema e o estado da mídia. Informamos o prazo junto com o orçamento, depois do diagnóstico — antes disso qualquer número seria chute."),
   ("Meus arquivos ficam seguros e privados?","Sim. Os dados são tratados com confidencialidade, usados apenas para a recuperação e devolvidos a você. Nada é compartilhado com terceiros."),
   ("O que eu faço agora para não piorar?","Desligue o equipamento e não instale programas de recuperação por conta própria — eles gravam no mesmo disco e podem sobrescrever justamente o que você quer recuperar. Fale conosco antes.")
 ]
},
{
 "slug":"suporte-tecnico-balneario-camboriu.html",
 "nav":"Suporte Técnico",
 "h1":"Suporte Técnico e Manutenção de Sistemas em Balneário Camboriú",
 "title":"Suporte Técnico de TI em Balneário Camboriú/SC — Soluções da Internet",
 "desc":"Suporte técnico de TI para empresas em Balneário Camboriú e Camboriú: manutenção de computadores, redes, servidores e sistemas, com atendimento presencial e remoto.",
 "sub":"Computadores lentos, rede caindo, sistema travando. Cuidamos da TI da sua empresa para que ela simplesmente funcione — presencialmente em Balneário Camboriú e Camboriú, e remotamente no resto do Brasil.",
 "svc_name":"Suporte Técnico e Manutenção de TI",
 "cities":["Balneário Camboriú","Camboriú"],
 "intro":[
   "Quando a TI para, a empresa inteira para junto. A <strong>Soluções da Internet</strong> oferece suporte técnico para negócios de <strong>Balneário Camboriú e Camboriú</strong>: computadores, redes, servidores e os sistemas do dia a dia.",
   "Atendemos tanto por demanda — quando algo quebra e precisa ser resolvido agora — quanto de forma <strong>contínua</strong>, acompanhando a estrutura para evitar que o problema aconteça."
 ],
 "incl_title":"O que atendemos",
 "incl":[
   "<strong>Manutenção de computadores e notebooks</strong> — limpeza, formatação, troca de peças e otimização de desempenho.",
   "<strong>Redes e Wi-Fi</strong> — instalação, configuração e correção de instabilidade e pontos sem sinal.",
   "<strong>Servidores e compartilhamento de arquivos</strong> entre os computadores da empresa.",
   "<strong>Backup automatizado</strong> — para que uma pane não vire prejuízo.",
   "<strong>Instalação e configuração de sistemas</strong>, e-mails corporativos e impressoras em rede.",
   "<strong>Remoção de vírus</strong> e configuração de segurança básica.",
   "<strong>Atendimento remoto</strong> — boa parte dos chamados é resolvida na hora, sem esperar deslocamento."
 ],
 "steps_title":"Como funciona",
 "steps":[
   ("Chamado","Você aciona por WhatsApp e descreve o problema. Respondemos rápido."),
   ("Diagnóstico","Identificamos a causa — remotamente sempre que possível, presencialmente quando necessário."),
   ("Resolução","Corrigimos e explicamos em português claro o que aconteceu e por quê."),
   ("Prevenção","Sugerimos o que ajustar para o mesmo problema não voltar.")
 ],
 "faq":[
   ("Vocês atendem presencialmente?","Sim, em Balneário Camboriú e Camboriú. Boa parte dos chamados, porém, é resolvida remotamente — o que costuma ser mais rápido, porque não depende de deslocamento. Por isso conseguimos atender também empresas de fora dessas duas cidades."),
   ("Trabalham com contrato mensal ou só por chamado?","Os dois. Você pode nos acionar pontualmente quando surgir um problema, ou contratar acompanhamento contínuo, que sai mais em conta para quem depende da TI no dia a dia e evita paradas."),
   ("Atendem empresas pequenas?","Sim. Boa parte dos nossos clientes são pequenos negócios com poucos computadores, que não têm um técnico próprio e precisam de alguém de confiança para chamar."),
   ("Qual o horário de atendimento?","Atendemos de segunda a sábado, das 8h às 20h — inclusive no sábado, quando muita empresa fica sem quem chamar, e até as 20h, o que ajuda quem só consegue parar para resolver TI depois do expediente."),
   ("Qual o tempo de resposta?","Chamados remotos costumam ser os mais rápidos, já que começam assim que recebemos a mensagem dentro do horário de atendimento. Para quem tem acompanhamento contínuo, o tempo de resposta é acordado em contrato, por escrito — em vez de ficar no informal."),
   ("Vocês cuidam também do site e dos sistemas?","Sim. Além da infraestrutura, desenvolvemos e damos manutenção em sites, sistemas e automações — então dá para resolver tudo com um único contato.")
 ]
},
{
 "slug":"automacao-de-processos-balneario-camboriu.html",
 "nav":"Automação de Processos",
 "h1":"Automação de Processos para Empresas em Balneário Camboriú",
 "title":"Automação de Processos e Integrações em Balneário Camboriú/SC — Soluções da Internet",
 "desc":"Automação de processos e integração de sistemas para empresas de Balneário Camboriú: elimine tarefas manuais, conecte planilhas, ERPs e plataformas via API.",
 "sub":"Aquela planilha que alguém preenche na mão todo dia, o relatório copiado de um sistema para outro, o e-mail enviado um por um. Isso pode virar automático.",
 "svc_name":"Automação de Processos e Integrações",
 "cities":["Balneário Camboriú","Camboriú"],
 "intro":[
   "Toda empresa tem tarefas repetitivas que consomem horas e ainda geram erro de digitação. A <strong>Soluções da Internet</strong> mapeia esses processos em negócios de <strong>Balneário Camboriú e Camboriú</strong> — e, à distância, em qualquer lugar do Brasil — e transforma o que é manual em automático.",
   "O resultado prático é simples: sua equipe para de gastar tempo com trabalho mecânico e passa a usar esse tempo no que realmente gera receita."
 ],
 "incl_title":"O que dá para automatizar",
 "incl":[
   "<strong>Integração entre sistemas</strong> — ERP, CRM, e-commerce e planilhas conversando entre si via API, sem redigitação.",
   "<strong>Relatórios automáticos</strong> — os números chegam prontos no seu e-mail ou WhatsApp, na frequência que você definir.",
   "<strong>Cadastro e atualização de dados</strong> — o que era copiado manualmente de um lugar para outro passa a ser sincronizado.",
   "<strong>Disparo de mensagens</strong> — confirmações, lembretes e follow-ups enviados automaticamente.",
   "<strong>Emissão e organização de documentos</strong> — propostas, contratos e planilhas geradas a partir dos dados que você já tem.",
   "<strong>Dashboards em tempo real</strong> — os indicadores do negócio em uma tela, atualizados sozinhos."
 ],
 "steps_title":"Como funciona",
 "steps":[
   ("Mapeamento","Acompanhamos como o processo funciona hoje e medimos quanto tempo ele consome."),
   ("Proposta","Mostramos o que dá para automatizar, o ganho esperado e o custo — com escopo fechado."),
   ("Construção","Desenvolvemos e testamos a automação com os seus dados reais, sem risco para a operação."),
   ("Acompanhamento","Colocamos no ar, treinamos a equipe e monitoramos para garantir que continue rodando.")
 ],
 "faq":[
   ("Minha empresa é pequena, vale a pena automatizar?","Geralmente sim, e às vezes vale ainda mais: em equipes pequenas, cada hora perdida com tarefa repetitiva pesa muito. Mapeamos o processo antes e só recomendamos automatizar quando o ganho compensa claramente o investimento."),
   ("Preciso trocar os sistemas que já uso?","Não. Na maioria dos casos conectamos o que você já usa. A troca de sistema só entra em discussão se o atual não permitir nenhuma integração — e isso é dito com clareza no diagnóstico."),
   ("E se a automação parar de funcionar?","Automações quebram quando um sistema conectado muda. Por isso oferecemos acompanhamento: monitoramos o funcionamento e corrigimos quando necessário."),
   ("Quanto tempo leva?","Depende de quantos sistemas estão envolvidos e de quanto eles facilitam a integração. Uma automação isolada é bem mais rápida do que conectar várias plataformas entre si. O prazo é fechado no escopo, depois do mapeamento."),
   ("Vocês trabalham com inteligência artificial?","Sim. Quando faz sentido para o processo, usamos IA — por exemplo em chatbots de atendimento, leitura de documentos e classificação automática de mensagens.")
 ]
},
{
 "slug":"chatbot-whatsapp-ia-balneario-camboriu.html",
 "nav":"Chatbots com IA",
 "h1":"Chatbot com IA para WhatsApp em Balneário Camboriú",
 "title":"Chatbot com IA para WhatsApp em Balneário Camboriú/SC — Soluções da Internet",
 "desc":"Criação de chatbots com inteligência artificial para WhatsApp e site em Balneário Camboriú: atendimento automático 24 horas, qualificação de clientes e agendamentos.",
 "sub":"Atendimento automático 24 horas no WhatsApp e no site, que responde as dúvidas de sempre, qualifica o cliente e só chama você quando a conversa realmente exige.",
 "svc_name":"Chatbots com Inteligência Artificial",
 "cities":["Balneário Camboriú","Camboriú"],
 "intro":[
   "A maior parte das mensagens que uma empresa recebe é repetida: horário de funcionamento, preço, prazo, endereço. Responder tudo isso manualmente consome o dia — e mensagem não respondida rápido vira cliente perdido para o concorrente.",
   "A <strong>Soluções da Internet</strong> desenvolve chatbots com inteligência artificial para negócios de <strong>Balneário Camboriú e Camboriú</strong>, e remotamente para todo o Brasil, treinados com as informações reais do seu negócio — não com respostas genéricas."
 ],
 "incl_title":"O que o chatbot faz",
 "incl":[
   "<strong>Responde 24 horas por dia</strong> — inclusive de madrugada, fim de semana e feriado.",
   "<strong>Entende linguagem natural</strong> — o cliente escreve do jeito dele, sem precisar digitar um número em um menu engessado.",
   "<strong>Qualifica o contato</strong> — descobre o que a pessoa quer antes de passar para você, e já chega com o contexto.",
   "<strong>Agenda horários e orçamentos</strong>, integrando com a sua agenda.",
   "<strong>Transfere para o atendente humano</strong> quando a conversa foge do escopo — sem deixar o cliente preso no robô.",
   "<strong>Funciona no WhatsApp e no site</strong>, com o mesmo conteúdo nos dois canais.",
   "<strong>Registra tudo</strong> — você vê o que os clientes mais perguntam e usa isso para melhorar o negócio."
 ],
 "steps_title":"Como funciona",
 "steps":[
   ("Levantamento","Reunimos as perguntas que você mais recebe e as informações corretas do seu negócio."),
   ("Treinamento","Configuramos a IA com esse conteúdo e definimos quando ela deve chamar um humano."),
   ("Testes","Testamos com conversas reais e ajustamos as respostas antes de liberar para os clientes."),
   ("Ajuste contínuo","Depois no ar, acompanhamos as conversas e refinamos o que não ficou bom.")
 ],
 "faq":[
   ("O cliente vai perceber que é um robô?","Ele vai perceber que o atendimento é rápido e que as respostas fazem sentido. Não escondemos que é um assistente automático — isso gera confiança — e deixamos sempre visível o caminho para falar com uma pessoa."),
   ("E se o chatbot responder errado?","Ele é treinado apenas com as informações do seu negócio e configurado para transferir ao humano quando a pergunta sai do escopo, em vez de inventar resposta. Durante as primeiras semanas acompanhamos as conversas e ajustamos o que for necessário."),
   ("Funciona no meu WhatsApp atual?","Sim, na maioria dos casos. Avaliamos a sua configuração — WhatsApp comum ou Business — e indicamos o caminho adequado, incluindo a API oficial quando o volume justificar."),
   ("Quanto custa? Tem mensalidade?","Sim, tem mensalidade. Um chatbot não é um produto que se instala e acaba: ele fica no ar 24 horas, consome os serviços de inteligência artificial a cada conversa e precisa de ajuste conforme o negócio muda — e é isso que a mensalidade cobre. O valor depende de quantas situações o robô precisa atender e de quais sistemas ele vai conversar. Levantamos isso antes e apresentamos tudo discriminado no orçamento, para você não descobrir custo recorrente depois de fechar."),
   ("Vou deixar de atender pessoalmente meus clientes?","Não é a ideia. O chatbot cuida do que é repetitivo e do que chega fora do horário; você continua atendendo o que importa — só que com o cliente já qualificado e sem perder mensagem.")
 ]
},
{
 "slug":"landing-pages-balneario-camboriu.html",
 "nav":"Landing Pages",
 "h1":"Criação de Landing Pages em Balneário Camboriú",
 "title":"Criação de Landing Pages em Balneário Camboriú/SC — Soluções da Internet",
 "desc":"Criação de landing pages de alta conversão em Balneário Camboriú: páginas focadas em campanhas de anúncios, lançamentos e captação de clientes, prontas para medir resultado.",
 "sub":"Uma página só, com um objetivo só: fazer o visitante agir. Feita para campanhas de anúncios, lançamentos e captação de contatos — e preparada para você medir o que cada real investido trouxe de volta.",
 "svc_name":"Criação de Landing Pages",
 "cities":["Balneário Camboriú","Camboriú"],
 "intro":[
   "Mandar tráfego pago para a home do site costuma ser desperdício: a home tem menu, serviços, rodapé e dez caminhos possíveis. Quem chegou por um anúncio específico se perde no meio disso e vai embora.",
   "A <strong>landing page</strong> resolve exatamente isso. É uma página única, sem distração, construída em torno de uma só ação — pedir orçamento, se inscrever, baixar algo, chamar no WhatsApp. A <strong>Soluções da Internet</strong> desenvolve landing pages para negócios de <strong>Balneário Camboriú e Camboriú</strong>, e remotamente para todo o Brasil."
 ],
 "incl_title":"O que está incluído",
 "incl":[
   "<strong>Uma única ação em foco</strong> — a página inteira é escrita e organizada para conduzir a esse objetivo, sem menu ou link que disperse o visitante.",
   "<strong>Carregamento rápido</strong> — página leve, porque em campanha paga cada segundo de espera é dinheiro de anúncio que você já gastou e perdeu.",
   "<strong>Feita para o celular primeiro</strong> — é de onde vem a maior parte do tráfego de anúncios.",
   "<strong>Formulário ou WhatsApp direto</strong> — o contato chega por onde for mais prático para você atender.",
   "<strong>Medição configurada</strong> — Google Analytics e o pixel da plataforma de anúncios instalados, para você saber quantos contatos cada campanha gerou.",
   "<strong>Texto orientado a conversão</strong> — estruturamos os argumentos, a prova e a chamada para ação; você revisa e ajusta o que não soar como você.",
   "<strong>Domínio e hospedagem configurados</strong>, com certificado de segurança (HTTPS)."
 ],
 "steps_title":"Como funciona o processo",
 "steps":[
   ("Objetivo","Definimos qual é a única ação que a página precisa gerar e para quem ela fala. Isso decide todo o resto."),
   ("Estrutura","Montamos a ordem dos argumentos: o problema, a solução, a prova e a chamada para ação."),
   ("Construção","Desenvolvemos a página, instalamos a medição e testamos o formulário de ponta a ponta."),
   ("Ajuste","Com a campanha rodando, olhamos os números reais e afinamos o que não estiver convertendo.")
 ],
 "faq":[
   ("Qual a diferença entre uma landing page e um site?","O site apresenta o negócio inteiro e serve a vários objetivos — quem chega nele pode estar procurando qualquer coisa. A landing page tem um objetivo só e nenhum caminho alternativo, por isso converte melhor o tráfego de uma campanha específica. Não são concorrentes: o site é a sua presença permanente, a landing page é a ferramenta da campanha. Se você precisa da presença completa, veja nossa página de criação de sites."),
   ("Quanto tempo leva para ficar pronto?","Uma landing page é o formato mais rápido que entregamos — costuma ficar perto de uma semana, dentro da faixa de 1 a 3 semanas que vale para os nossos projetos de site. O que mais influencia é a velocidade na definição da oferta e na aprovação do texto."),
   ("Preciso já ter campanha de anúncios rodando?","Não, mas a landing page rende muito mais quando existe tráfego direcionado chegando nela. Se você ainda não anuncia, vale conversar sobre isso antes, para a página não ficar pronta e sem visitantes."),
   ("Vocês garantem quantos clientes a página vai trazer?","Não, e desconfie de quem garantir. O resultado depende da sua oferta, do preço, do público e do investimento em anúncios — a página é uma parte importante disso, não o todo. O que fazemos é construir a página com as boas práticas de conversão e deixar a medição configurada, para que a decisão seguinte seja tomada com número e não com achismo."),
   ("Dá para testar versões diferentes da página?","Sim. Com a medição configurada, é possível publicar variações e comparar qual converte melhor. Costuma ser o passo seguinte, depois que a primeira versão acumulou visitas suficientes para a comparação significar alguma coisa.")
 ]
}
]

ICON = ('<svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true">'
        '<path d="M16.02 3C9.4 3 4.02 8.37 4.02 15c0 2.23.6 4.35 1.75 6.22L3 29l7.98-2.7A11.9 11.9 0 0 0 16.02 27C22.63 27 28 21.63 28 15S22.63 3 16.02 3Zm0 21.6c-1.86 0-3.66-.5-5.23-1.44l-.37-.22-4.7 1.59 1.6-4.58-.24-.38A9.53 9.53 0 0 1 5.62 15c0-5.2 4.2-9.4 9.4-9.4S24.4 9.8 24.4 15s-4.2 9.6-9.38 9.6Zm5.15-7.2c-.28-.14-1.66-.82-1.92-.91-.26-.1-.44-.14-.63.14-.19.28-.72.91-.88 1.1-.16.19-.32.21-.6.07-.28-.14-1.17-.43-2.24-1.38-.83-.74-1.38-1.65-1.55-1.93-.16-.28-.02-.43.12-.57.13-.13.28-.33.42-.5.14-.16.19-.28.28-.47.09-.19.05-.35-.02-.5-.07-.14-.63-1.52-.87-2.08-.23-.55-.46-.48-.63-.49h-.54c-.19 0-.5.07-.76.35-.26.28-1 .98-1 2.38 0 1.4 1.02 2.76 1.16 2.95.14.19 2.01 3.07 4.87 4.3.68.29 1.21.47 1.63.6.68.22 1.3.19 1.79.11.55-.08 1.66-.68 1.89-1.33.24-.66.24-1.22.16-1.34-.07-.12-.26-.19-.54-.33Z"/></svg>')

TEMPLATE = u'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<meta name="author" content="Soluções da Internet">
<meta name="theme-color" content="#0f1720">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{base}assets/img/logo-icon-512.png">
<meta property="og:url" content="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Soluções da Internet">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{base}assets/img/logo-icon-512.png">
<link rel="canonical" href="{url}">
<link rel="icon" href="assets/img/logo-icon-512.png" type="image/png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css?v={cssv}">
<script type="application/ld+json">
{ldj}
</script>
</head>
<body>

<div class="bg-aurora" aria-hidden="true">
  <span class="aurora a1"></span>
  <span class="aurora a2"></span>
  <span class="aurora a3"></span>
</div>

<header class="site-header" id="siteHeader">
  <div class="container header-inner">
    <a href="index.html" class="brand" aria-label="Soluções da Internet">
      <span class="brand-icon-wrap">
        <img src="assets/img/logo-icon.png" alt="" class="brand-icon">
      </span>
      <span class="brand-word">Soluções <em class="accent">da Internet</em></span>
    </a>

    <nav class="main-nav" id="mainNav">
      <a href="index.html#servicos">Serviços</a>
      <a href="index.html#processo">Como funciona</a>
      <a href="index.html#numeros">Resultados</a>
      <a href="index.html#contato">Contato</a>
    </nav>

    <div class="header-actions" aria-label="Ações rápidas">
      <a href="https://wa.me/5547992607105" target="_blank" rel="noopener" class="whatsapp-float" aria-label="Falar no WhatsApp">
        <span class="whatsapp-pulse" aria-hidden="true"></span>
        {icon}
      </a>
    </div>

    <a href="index.html#contato" class="btn btn-primary btn-small nav-cta">Fale conosco</a>

    <button class="menu-toggle" id="menuToggle" aria-label="Abrir menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<main class="svc-page">

  <section class="section" style="padding-top: 20px">
    <div class="container">
      <nav class="breadcrumbs" aria-label="Você está aqui">
        <a href="index.html">Início</a><span>&rsaquo;</span><a href="index.html#servicos">Serviços</a><span>&rsaquo;</span>{nav}
      </nav>
      <div class="svc-hero">
        <p class="eyebrow reveal">Soluções da Internet</p>
        <h1>{h1}</h1>
        <p class="hero-sub reveal" style="--delay: 0.12s">{sub}</p>
        <div class="hero-actions reveal" style="--delay: 0.2s">
          <a href="index.html#contato" class="btn btn-primary">Solicitar orçamento</a>
          <a href="https://wa.me/5547992607105" target="_blank" rel="noopener" class="btn btn-ghost">Falar no WhatsApp</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top: 24px">
    <div class="container svc-body reveal">
{intro}
    </div>
  </section>

  <section class="section" style="padding-top: 0">
    <div class="container svc-body reveal">
      <h2>{incl_title}</h2>
      <ul class="svc-list">
{incl}
      </ul>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head reveal">
        <h2>{steps_title}</h2>
      </div>
      <div class="service-grid">
{steps}
      </div>
    </div>
  </section>

  <section class="section" style="padding-top: 0">
    <div class="container svc-body">
      <div class="section-head reveal" style="margin-bottom: 32px">
        <h2>Perguntas frequentes</h2>
      </div>
      <div class="faq-list">
{faq}
      </div>
    </div>
  </section>

  <section class="section" style="padding-top: 0">
    <div class="container">
      <div class="section-head reveal" style="margin-bottom: 24px">
        <h2>Outros serviços</h2>
      </div>
      <div class="svc-related reveal">
{rel}
      </div>
    </div>
  </section>

  <section class="section cta-band">
    <div class="container cta-inner reveal">
      <h2>Vamos conversar sobre o seu projeto?</h2>
      <p>Conte o que você precisa e receba um orçamento gratuito, sem compromisso.</p>
      <a href="index.html#contato" class="btn btn-primary">Solicitar orçamento gratuito</a>
    </div>
  </section>

</main>

<footer class="site-footer">
  <div class="container footer-inner">
    <a href="index.html" class="brand">
      <img src="assets/img/logo-icon.png" alt="" class="brand-icon">
      <span class="brand-word">Soluções <em class="accent">da Internet</em></span>
    </a>
    <p>&copy; <span id="year"></span> Soluções da Internet. Todos os direitos reservados.</p>
    <div class="footer-links">
      <a href="index.html#servicos">Serviços</a>
      <a href="index.html#contato">Contato</a>
      <a href="privacidade.html">Privacidade</a>
      <a href="termos.html">Termos de Uso</a>
    </div>
  </div>
</footer>

<script src="assets/js/script.js?v={cssv}"></script>
</body>
</html>
'''


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build(p, others):
    url = BASE + p["slug"]
    cities = p["cities"]
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Service", "@id": url + "#service", "name": p["svc_name"],
             "serviceType": p["svc_name"], "description": p["desc"], "url": url,
             "provider": {"@id": BASE + "#business"},
             "areaServed": [{"@type": "City", "name": n} for n in cities] +
                           [{"@type": "State", "name": "Santa Catarina"}],
             "availableChannel": {"@type": "ServiceChannel", "serviceUrl": url,
                                  "servicePhone": {"@type": "ContactPoint",
                                                   "telephone": "+55-47-99260-7105"}}},
            {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Início", "item": BASE},
                {"@type": "ListItem", "position": 2, "name": "Serviços", "item": BASE + "#servicos"},
                {"@type": "ListItem", "position": 3, "name": p["nav"], "item": url}]},
            {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]},
            {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": p["title"],
             "description": p["desc"], "inLanguage": "pt-BR",
             "isPartOf": {"@id": BASE + "#website"},
             "breadcrumb": {"@id": url + "#breadcrumb"},
             "about": {"@id": url + "#service"}}
        ]}

    intro = "\n".join("      <p>%s</p>" % t for t in p["intro"])
    incl = "\n".join("        <li>%s</li>" % i for i in p["incl"])
    steps = "\n".join(
        '        <article class="service-card reveal" style="--delay: %.2fs">\n'
        '          <div class="step-num">%d</div>\n'
        '          <h3>%s</h3>\n'
        '          <p>%s</p>\n'
        '        </article>' % (0.04 * n, n + 1, t, d)
        for n, (t, d) in enumerate(p["steps"]))
    faq = "\n".join(
        '        <div class="faq-item reveal" style="--delay: %.2fs">\n'
        '          <h3>%s</h3>\n'
        '          <p>%s</p>\n'
        '        </div>' % (0.04 * n, esc(q), esc(a))
        for n, (q, a) in enumerate(p["faq"]))
    rel = "\n".join('        <a href="%s">%s</a>' % (o["slug"], o["nav"]) for o in others)

    return TEMPLATE.format(
        title=p["title"], desc=p["desc"], url=url, base=BASE, cssv=CSSV,
        ldj=json.dumps(ld, ensure_ascii=False, indent=2), icon=ICON,
        nav=p["nav"], h1=p["h1"], sub=p["sub"], intro=intro,
        incl_title=p["incl_title"], incl=incl, steps_title=p["steps_title"],
        steps=steps, faq=faq, rel=rel)


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

for p in PAGES:
    others = [o for o in PAGES if o["slug"] != p["slug"]]
    destino = os.path.join(ROOT, p["slug"])
    io.open(destino, "w", encoding="utf-8").write(build(p, others))
    print("gerado: " + p["slug"])
