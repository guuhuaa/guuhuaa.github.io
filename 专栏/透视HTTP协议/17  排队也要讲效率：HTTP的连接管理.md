<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>17  排队也要讲效率：HTTP的连接管理.md</title>
        <!-- Spectre.css framework -->
        <link rel="stylesheet" href="../../static/index.css">
        <!-- theme css & js -->
        <meta name="generator" content="Hexo 4.2.0">
    </head>

<body>

<div class="book-container">
    <div class="book-sidebar">
        <div class="book-brand">
            <a href="../../index.html">
                <img src="../../static/favicon.png">
                <span>技术文章摘抄</span>
            </a>
        </div>
        <div class="book-menu uncollapsible">
            <ul class="uncollapsible">
                <li><a href="../../index.html" class="current-tab">首页</a></li>
            </ul>

            <ul class="uncollapsible">
                <li><a href="../index.html">上一级</a></li>
            </ul>

            <ul class="uncollapsible">
                <li>

                    
                    <a href="00&#32;开篇词｜To&#32;Be&#32;a&#32;HTTP&#32;Hero.md">00 开篇词｜To Be a HTTP Hero.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;时势与英雄：HTTP的前世今生.md">01  时势与英雄：HTTP的前世今生.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;HTTP是什么？HTTP又不是什么？.md">02  HTTP是什么？HTTP又不是什么？.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;HTTP世界全览（上）：与HTTP相关的各种概念.md">03  HTTP世界全览（上）：与HTTP相关的各种概念.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;HTTP世界全览（下）：与HTTP相关的各种协议.md">04  HTTP世界全览（下）：与HTTP相关的各种协议.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;常说的“四层”和“七层”到底是什么？“五层”“六层”哪去了？.md">05  常说的“四层”和“七层”到底是什么？“五层”“六层”哪去了？.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;域名里有哪些门道？.md">06  域名里有哪些门道？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;自己动手，搭建HTTP实验环境.md">07  自己动手，搭建HTTP实验环境.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;键入网址再按下回车，后面究竟发生了什么？.md">08  键入网址再按下回车，后面究竟发生了什么？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;HTTP报文是什么样子的？.md">09  HTTP报文是什么样子的？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;应该如何理解请求方法？.md">10  应该如何理解请求方法？.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;你能写出正确的网址吗？.md">11  你能写出正确的网址吗？.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;响应状态码该怎么用？.md">12  响应状态码该怎么用？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;HTTP有哪些特点？.md">13  HTTP有哪些特点？.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;HTTP有哪些优点？又有哪些缺点？.md">14  HTTP有哪些优点？又有哪些缺点？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;海纳百川：HTTP的实体数据.md">15  海纳百川：HTTP的实体数据.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;把大象装进冰箱：HTTP传输大文件的方法.md">16  把大象装进冰箱：HTTP传输大文件的方法.md</a>

                </li>
                <li>

                    <a class="current-tab" href="17&#32;&#32;排队也要讲效率：HTTP的连接管理.md">17  排队也要讲效率：HTTP的连接管理.md</a>
                    

                </li>
                <li>

                    
                    <a href="18&#32;&#32;四通八达：HTTP的重定向和跳转.md">18  四通八达：HTTP的重定向和跳转.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;让我知道你是谁：HTTP的Cookie机制.md">19  让我知道你是谁：HTTP的Cookie机制.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;生鲜速递：HTTP的缓存控制.md">20  生鲜速递：HTTP的缓存控制.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;良心中间商：HTTP的代理服务.md">21  良心中间商：HTTP的代理服务.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;冷链周转：HTTP的缓存代理.md">22  冷链周转：HTTP的缓存代理.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;&#32;HTTPS是什么？SSLTLS又是什么？.md">23  HTTPS是什么？SSLTLS又是什么？.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;&#32;固若金汤的根本（上）：对称加密与非对称加密.md">24  固若金汤的根本（上）：对称加密与非对称加密.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;&#32;固若金汤的根本（下）：数字签名与证书.md">25  固若金汤的根本（下）：数字签名与证书.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;&#32;信任始于握手：TLS1.2连接过程解析.md">26  信任始于握手：TLS1.2连接过程解析.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;&#32;更好更快的握手：TLS1.3特性解析.md">27  更好更快的握手：TLS1.3特性解析.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;&#32;连接太慢该怎么办：HTTPS的优化.md">28  连接太慢该怎么办：HTTPS的优化.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;&#32;我应该迁移到HTTPS吗？.md">29  我应该迁移到HTTPS吗？.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;&#32;时代之风（上）：HTTP2特性概览.md">30  时代之风（上）：HTTP2特性概览.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;&#32;时代之风（下）：HTTP2内核剖析.md">31  时代之风（下）：HTTP2内核剖析.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;&#32;未来之路：HTTP3展望.md">32  未来之路：HTTP3展望.md</a>

                </li>
                <li>

                    
                    <a href="33&#32;&#32;我应该迁移到HTTP2吗？.md">33  我应该迁移到HTTP2吗？.md</a>

                </li>
                <li>

                    
                    <a href="34&#32;&#32;Nginx：高性能的Web服务器.md">34  Nginx：高性能的Web服务器.md</a>

                </li>
                <li>

                    
                    <a href="35&#32;&#32;OpenResty：更灵活的Web服务器.md">35  OpenResty：更灵活的Web服务器.md</a>

                </li>
                <li>

                    
                    <a href="36&#32;&#32;WAF：保护我们的网络服务.md">36  WAF：保护我们的网络服务.md</a>

                </li>
                <li>

                    
                    <a href="37&#32;&#32;CDN：加速我们的网络服务.md">37  CDN：加速我们的网络服务.md</a>

                </li>
                <li>

                    
                    <a href="38&#32;&#32;WebSocket：沙盒里的TCP.md">38  WebSocket：沙盒里的TCP.md</a>

                </li>
                <li>

                    
                    <a href="39&#32;&#32;HTTP性能优化面面观（上）.md">39  HTTP性能优化面面观（上）.md</a>

                </li>
                <li>

                    
                    <a href="40&#32;&#32;HTTP性能优化面面观（下）.md">40  HTTP性能优化面面观（下）.md</a>

                </li>
                <li>

                    
                    <a href="结束语&#32;&#32;做兴趣使然的Hero.md">结束语  做兴趣使然的Hero.md</a>

                </li>
            </ul>

        </div>
    </div>

    <div class="sidebar-toggle" onclick="sidebar_toggle()" onmouseover="add_inner()" onmouseleave="remove_inner()">
        <div class="sidebar-toggle-inner"></div>
    </div>

    <script>
        function add_inner() {
            let inner = document.querySelector('.sidebar-toggle-inner')
            inner.classList.add('show')
        }

        function remove_inner() {
            let inner = document.querySelector('.sidebar-toggle-inner')
            inner.classList.remove('show')
        }

        function sidebar_toggle() {
            let sidebar_toggle = document.querySelector('.sidebar-toggle')
            let sidebar = document.querySelector('.book-sidebar')
            let content = document.querySelector('.off-canvas-content')
            if (sidebar_toggle.classList.contains('extend')) { // show
                sidebar_toggle.classList.remove('extend')
                sidebar.classList.remove('hide')
                content.classList.remove('extend')
            } else { // hide
                sidebar_toggle.classList.add('extend')
                sidebar.classList.add('hide')
                content.classList.add('extend')
            }
        }
    </script>

    <div class="off-canvas-content">
        <div class="columns">
            <div class="column col-12 col-lg-12">
                <div class="book-navbar">
                    <!-- For Responsive Layout -->
                    <header class="navbar">
                        <section class="navbar-section">
                            <a onclick="open_sidebar()">
                                <i class="icon icon-menu"></i>
                            </a>
                        </section>
                    </header>
                </div>
                <div class="book-content" style="max-width: 960px; margin: 0 auto;
    overflow-x: auto;
    overflow-y: hidden;">
                    <div class="book-post">
                        <p id="tip" align="center"></p>
                        <div><h1>17  排队也要讲效率：HTTP的连接管理</h1>
<p>在[第 14 讲]里，我曾经提到过 HTTP 的性能问题，用了六个字来概括：“<strong>不算差，不够好</strong>”。同时，我也谈到了“队头阻塞”，但由于时间的限制没有展开来细讲，这次就来好好地看看 HTTP 在连接这方面的表现。</p>
<p>HTTP 的连接管理也算得上是个“老生常谈”的话题了，你一定曾经听说过“短连接”“长连接”之类的名词，今天让我们一起来把它们弄清楚。</p>
<h2>短连接</h2>
<p>HTTP 协议最初（0.9/1.0）是个非常简单的协议，通信过程也采用了简单的“请求 - 应答”方式。</p>
<p>它底层的数据传输基于 TCP/IP，每次发送请求前需要先与服务器建立连接，收到响应报文后会立即关闭连接。</p>
<p>因为客户端与服务器的整个连接过程很短暂，不会与服务器保持长时间的连接状态，所以就被称为“<strong>短连接</strong>”（short-lived connections）。早期的 HTTP 协议也被称为是“<strong>无连接</strong>”的协议。</p>
<p>短连接的缺点相当严重，因为在 TCP 协议里，建立连接和关闭连接都是非常“昂贵”的操作。TCP 建立连接要有“三次握手”，发送 3 个数据包，需要 1 个 RTT；关闭连接是“四次挥手”，4 个数据包需要 2 个 RTT。</p>
<p>而 HTTP 的一次简单“请求 - 响应”通常只需要 4 个包，如果不算服务器内部的处理时间，最多是 2 个 RTT。这么算下来，浪费的时间就是“3÷5=60%”，有三分之二的时间被浪费掉了，传输效率低得惊人。</p>
<p><img src="assets/54315ed9ac37fbc6547258040f00a80c.png" alt="img" /></p>
<p>单纯地从理论上讲，TCP 协议你可能还不太好理解，我就拿打卡考勤机来做个形象的比喻吧。</p>
<p>假设你的公司买了一台打卡机，放在前台，因为这台机器比较贵，所以专门做了一个保护罩盖着它，公司要求每次上下班打卡时都要先打开盖子，打卡后再盖上盖子。</p>
<p>可是偏偏这个盖子非常牢固，打开关闭要费很大力气，打卡可能只要 1 秒钟，而开关盖子却需要四五秒钟，大部分时间都浪费在了毫无意义的开关盖子操作上了。</p>
<p>可想而知，平常还好说，一到上下班的点在打卡机前就会排起长队，每个人都要重复“开盖 - 打卡 - 关盖”的三个步骤，你说着急不着急。</p>
<p>在这个比喻里，打卡机就相当于服务器，盖子的开关就是 TCP 的连接与关闭，而每个打卡的人就是 HTTP 请求，很显然，短连接的缺点严重制约了服务器的服务能力，导致它无法处理更多的请求。</p>
<h2>长连接</h2>
<p>针对短连接暴露出的缺点，HTTP 协议就提出了“<strong>长连接</strong>”的通信方式，也叫“持久连接”（persistent connections）、“连接保活”（keep alive）、“连接复用”（connection reuse）。</p>
<p>其实解决办法也很简单，用的就是“<strong>成本均摊</strong>”的思路，既然 TCP 的连接和关闭非常耗时间，那么就把这个时间成本由原来的一个“请求 - 应答”均摊到多个“请求 - 应答”上。</p>
<p>这样虽然不能改善 TCP 的连接效率，但基于“<strong>分母效应</strong>”，每个“请求 - 应答”的无效时间就会降低不少，整体传输效率也就提高了。</p>
<p>这里我画了一个短连接与长连接的对比示意图。</p>
<p><img src="assets/57b3d80234a1f1b8c538a376aa01d3b4.png" alt="img" /></p>
<p>在短连接里发送了三次 HTTP“请求 - 应答”，每次都会浪费 60% 的 RTT 时间。而在长连接的情况下，同样发送三次请求，因为只在第一次时建立连接，在最后一次时关闭连接，所以浪费率就是“3÷9≈33%”，降低了差不多一半的时间损耗。显然，如果在这个长连接上发送的请求越多，分母就越大，利用率也就越高。</p>
<p>继续用刚才的打卡机的比喻，公司也觉得这种反复“开盖 - 打卡 - 关盖”的操作太“反人类”了，于是颁布了新规定，早上打开盖子后就不用关上了，可以自由打卡，到下班后再关上盖子。</p>
<p>这样打卡的效率（即服务能力）就大幅度提升了，原来一次打卡需要五六秒钟，现在只要一秒就可以了，上下班时排长队的景象一去不返，大家都开心。</p>
<h2>连接相关的头字段</h2>
<p>由于长连接对性能的改善效果非常显著，所以在 HTTP/1.1 中的连接都会默认启用长连接。不需要用什么特殊的头字段指定，只要向服务器发送了第一次请求，后续的请求都会重复利用第一次打开的 TCP 连接，也就是长连接，在这个连接上收发数据。</p>
<p>当然，我们也可以在请求头里明确地要求使用长连接机制，使用的字段是<strong>Connection</strong>，值是“<strong>keep-alive</strong>”。</p>
<p>不过不管客户端是否显式要求长连接，如果服务器支持长连接，它总会在响应报文里放一个“<strong>Connection: keep-alive</strong>”字段，告诉客户端：“我是支持长连接的，接下来就用这个 TCP 一直收发数据吧”。</p>
<p>你可以在实验环境里访问 URI“/17-1”，用 Chrome 看一下服务器返回的响应头：</p>
<p><img src="assets/27f13aacad9704368ce383b764c46bc6.png" alt="img" /></p>
<p>不过长连接也有一些小缺点，问题就出在它的“长”字上。</p>
<p>因为 TCP 连接长时间不关闭，服务器必须在内存里保存它的状态，这就占用了服务器的资源。如果有大量的空闲长连接只连不发，就会很快耗尽服务器的资源，导致服务器无法为真正有需要的用户提供服务。</p>
<p>所以，长连接也需要在恰当的时间关闭，不能永远保持与服务器的连接，这在客户端或者服务器都可以做到。</p>
<p>在客户端，可以在请求头里加上“<strong>Connection: close</strong>”字段，告诉服务器：“这次通信后就关闭连接”。服务器看到这个字段，就知道客户端要主动关闭连接，于是在响应报文里也加上这个字段，发送之后就调用 Socket API 关闭 TCP 连接。</p>
<p>服务器端通常不会主动关闭连接，但也可以使用一些策略。拿 Nginx 来举例，它有两种方式：</p>
<ol>
<li>使用“keepalive_timeout”指令，设置长连接的超时时间，如果在一段时间内连接上没有任何数据收发就主动断开连接，避免空闲连接占用系统资源。</li>
<li>使用“keepalive_requests”指令，设置长连接上可发送的最大请求次数。比如设置成 1000，那么当 Nginx 在这个连接上处理了 1000 个请求后，也会主动断开连接。</li>
</ol>
<p>另外，客户端和服务器都可以在报文里附加通用头字段“Keep-Alive: timeout=value”，限定长连接的超时时间。但这个字段的约束力并不强，通信的双方可能并不会遵守，所以不太常见。</p>
<p>我们的实验环境配置了“keepalive_timeout 60”和“keepalive_requests 5”，意思是空闲连接最多 60 秒，最多发送 5 个请求。所以，如果连续刷新五次页面，就能看到响应头里的“Connection: close”了。</p>
<p>把这个过程用 Wireshark 抓一下包，就能够更清晰地看到整个长连接中的握手、收发数据与挥手过程，在课后你可以再实际操作看看。</p>
<p><img src="assets/ecfb04b7a97f3591efedc428800a4845.png" alt="img" /></p>
<h2>队头阻塞</h2>
<p>看完了短连接和长连接，接下来就要说到著名的“队头阻塞”（Head-of-line blocking，也叫“队首阻塞”）了。</p>
<p>“队头阻塞”与短连接和长连接无关，而是由 HTTP 基本的“请求 - 应答”模型所导致的。</p>
<p>因为 HTTP 规定报文必须是“一发一收”，这就形成了一个先进先出的“串行”队列。队列里的请求没有轻重缓急的优先级，只有入队的先后顺序，排在最前面的请求被最优先处理。</p>
<p>如果队首的请求因为处理的太慢耽误了时间，那么队列里后面的所有请求也不得不跟着一起等待，结果就是其他的请求承担了不应有的时间成本。</p>
<p><img src="assets/6a6d30a89fb085d5f1773a887aaf5572.png" alt="img" /></p>
<p>还是用打卡机做个比喻。</p>
<p>上班的时间点上，大家都在排队打卡，可这个时候偏偏最前面的那个人遇到了打卡机故障，怎么也不能打卡成功，急得满头大汗。等找人把打卡机修好，后面排队的所有人全迟到了。</p>
<h2>性能优化</h2>
<p>因为“请求 - 应答”模型不能变，所以“队头阻塞”问题在 HTTP/1.1 里无法解决，只能缓解，有什么办法呢？</p>
<p>公司里可以再多买几台打卡机放在前台，这样大家可以不用挤在一个队伍里，分散打卡，一个队伍偶尔阻塞也不要紧，可以改换到其他不阻塞的队伍。</p>
<p>这在 HTTP 里就是“<strong>并发连接</strong>”（concurrent connections），也就是同时对一个域名发起多个长连接，用数量来解决质量的问题。</p>
<p>但这种方式也存在缺陷。如果每个客户端都想自己快，建立很多个连接，用户数×并发数就会是个天文数字。服务器的资源根本就扛不住，或者被服务器认为是恶意攻击，反而会造成“拒绝服务”。</p>
<p>所以，HTTP 协议建议客户端使用并发，但不能“滥用”并发。RFC2616 里明确限制每个客户端最多并发 2 个连接。不过实践证明这个数字实在是太小了，众多浏览器都“无视”标准，把这个上限提高到了 6~8。后来修订的 RFC7230 也就“顺水推舟”，取消了这个“2”的限制。</p>
<p>但“并发连接”所压榨出的性能也跟不上高速发展的互联网无止境的需求，还有什么别的办法吗？</p>
<p>公司发展的太快了，员工越来越多，上下班打卡成了迫在眉睫的大问题。前台空间有限，放不下更多的打卡机了，怎么办？那就多开几个打卡的地方，每个楼层、办公区的入口也放上三四台打卡机，把人进一步分流，不要都往前台挤。</p>
<p>这个就是“<strong>域名分片</strong>”（domain sharding）技术，还是用数量来解决质量的思路。</p>
<p>HTTP 协议和浏览器不是限制并发连接数量吗？好，那我就多开几个域名，比如 shard1.chrono.com、shard2.chrono.com，而这些域名都指向同一台服务器 www.chrono.com，这样实际长连接的数量就又上去了，真是“美滋滋”。不过实在是有点“上有政策，下有对策”的味道。</p>
<h2>小结</h2>
<p>这一讲中我们学习了 HTTP 协议里的短连接和长连接，简单小结一下今天的内容：</p>
<ol>
<li>早期的 HTTP 协议使用短连接，收到响应后就立即关闭连接，效率很低；</li>
<li>HTTP/1.1 默认启用长连接，在一个连接上收发多个请求响应，提高了传输效率；</li>
<li>服务器会发送“Connection: keep-alive”字段表示启用了长连接；</li>
<li>报文头里如果有“Connection: close”就意味着长连接即将关闭；</li>
<li>过多的长连接会占用服务器资源，所以服务器会用一些策略有选择地关闭长连接；</li>
<li>“队头阻塞”问题会导致性能下降，可以用“并发连接”和“域名分片”技术缓解。</li>
</ol>
<h2>课下作业</h2>
<ol>
<li>在开发基于 HTTP 协议的客户端时应该如何选择使用的连接模式呢？短连接还是长连接？</li>
<li>应当如何降低长连接对服务器的负面影响呢？</li>
</ol>
<p>欢迎你把自己的学习体会写在留言区，与我和其他同学一起讨论。如果你觉得有所收获，也欢迎把文章分享给你的朋友。</p>
<p><img src="assets/f93afe4b663d681b8ce63c947f478072.png" alt="unpreview" /></p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="16&#32;&#32;把大象装进冰箱：HTTP传输大文件的方法.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="18&#32;&#32;四通八达：HTTP的重定向和跳转.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435c3d8ad6645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
</body>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-NPSEEVD756"></script>
<script>
    window.dataLayer = window.dataLayer || [];

    function gtag() {
        dataLayer.push(arguments);
    }

    gtag('js', new Date());
    gtag('config', 'G-NPSEEVD756');
    var path = window.location.pathname
    var cookie = getCookie("lastPath");
    console.log(path)
    if (path.replace("/", "") === "") {
        if (cookie.replace("/", "") !== "") {
            console.log(cookie)
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E9%80%8F%E8%A7%86HTTP%E5%8D%8F%E8%AE%AE/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
        }
    } else {
        setCookie("lastPath", path)
    }

    function setCookie(cname, cvalue) {
        var d = new Date();
        d.setTime(d.getTime() + (180 * 24 * 60 * 60 * 1000));
        var expires = "expires=" + d.toGMTString();
        document.cookie = cname + "=" + cvalue + "; " + expires + ";path = /";
    }

    function getCookie(cname) {
        var name = cname + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i].trim();
            if (c.indexOf(name) === 0) return c.substring(name.length, c.length);
        }
        return "";
    }
</script>

</html>
