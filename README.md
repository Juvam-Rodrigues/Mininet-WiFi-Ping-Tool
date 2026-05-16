<h1>🌐 Mininet-WiFi Ping Tool</h1>

<h2>📝 Descrição</h2>

<p>
Projeto em Python desenvolvido para auxiliar testes de conectividade entre hosts no Mininet-WiFi.
</p>

<p>
A ferramenta realiza ping automático entre todos os hosts da rede, exibindo os IPs atualizados em tempo real utilizando <code>hostname -I</code>, evitando problemas de IPs desatualizados comuns no Mininet-WiFi.
</p>

<p>
Além disso, o sistema calcula a taxa de sucesso das conexões realizadas entre os hosts.
</p>

<hr>

<h2>⚙️ Funcionalidades</h2>

<ul>
    <li>Ping automático entre todos os hosts da rede</li>
    <li>Exibição do nome e IP atualizado dos hosts</li>
    <li>Ignora ping para o próprio host</li>
    <li>Utiliza <code>hostname -I</code> para obter IPs reais e atualizados</li>
    <li>Calcula taxa de sucesso da conectividade da rede</li>
    <li>Exibe resultado individual de cada teste (<code>OK</code> ou <code>FALHOU</code>)</li>
</ul>

<hr>

<h2>🚀 Como usar</h2>

<h3>1️⃣ Adicione o arquivo ao projeto</h3>

<p>
Salve o arquivo Python como:
</p>

<pre><code>meuping.py</code></pre>

<p>
na mesma pasta do seu projeto Mininet-WiFi.
</p>

<h3>2️⃣ Execute o Mininet-WiFi</h3>

<p>
Inicie normalmente sua topologia Mininet-WiFi.
</p>

<h3>3️⃣ Carregue o script no CLI</h3>

<p>
No terminal do Mininet-WiFi, execute:
</p>

<pre><code>py __import__('meuping').pingTodos(net)</code></pre>

<hr>

<h2>📌 Exemplo de saída</h2>

<pre><code>
h1 - 192.168.0.1 ---> h2 - 192.168.0.2: OK
h1 - 192.168.0.1 ---> h3 - 192.168.0.3: OK
h2 - 192.168.0.2 ---> h1 - 192.168.0.1: OK

Taxa de sucesso: 100.00% (6/6)
</code></pre>

<hr>

<h2>🧠 Como funciona</h2>

<p>
O sistema utiliza o comando Linux:
</p>

<pre><code>hostname -I</code></pre>

<p>
para obter os IPs atuais dos hosts diretamente do sistema operacional do namespace Linux do Mininet-WiFi.
</p>

<p>
Isso evita inconsistências causadas por <code>host.IP()</code>, que pode retornar IPs desatualizados em cenários com múltiplas interfaces ou alterações dinâmicas de rede.
</p>

<hr>

<h2>📂 Estrutura do projeto</h2>

<pre><code>
Projeto/
 ├─ meuping.py
 └─ topologia.py
</code></pre>

<hr>

<h2>🔧 Tecnologias utilizadas</h2>

<ul>
    <li>Python</li>
    <li>Mininet-WiFi</li>
    <li>Linux Networking</li>
    <li>ICMP/Ping</li>
</ul>

<hr>

<h2>👤 Autor</h2>

<p>
Juvam Rodrigues do Nascimento Neto (https://github.com/Juvam-Rodrigues ).
</p>
