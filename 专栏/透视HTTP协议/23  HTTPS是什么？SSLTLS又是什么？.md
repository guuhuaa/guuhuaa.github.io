<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>23  HTTPS是什么？SSLTLS又是什么？.md</title>
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

                    
                    <a href="17&#32;&#32;排队也要讲效率：HTTP的连接管理.md">17  排队也要讲效率：HTTP的连接管理.md</a>

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

                    <a class="current-tab" href="23&#32;&#32;HTTPS是什么？SSLTLS又是什么？.md">23  HTTPS是什么？SSLTLS又是什么？.md</a>
                    

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
                        <div><h1>23  HTTPS是什么？SSLTLS又是什么？</h1>
<p>从今天开始，我们开始进入全新的“安全篇”，聊聊与安全相关的 HTTPS、SSL、TLS。</p>
<p>在[第 14 讲]中，我曾经谈到过 HTTP 的一些缺点，其中的“无状态”在加入 Cookie 后得到了解决，而另两个缺点——“明文”和“不安全”仅凭 HTTP 自身是无力解决的，需要引入新的 HTTPS 协议。</p>
<h2>为什么要有 HTTPS？</h2>
<p>简单的回答是“<strong>因为 HTTP 不安全</strong>”。</p>
<p>由于 HTTP 天生“明文”的特点，整个传输过程完全透明，任何人都能够在链路中截获、修改或者伪造请求 / 响应报文，数据不具有可信性。</p>
<p>比如，前几讲中说过的“代理服务”。它作为 HTTP 通信的中间人，在数据上下行的时候可以添加或删除部分头字段，也可以使用黑白名单过滤 body 里的关键字，甚至直接发送虚假的请求、响应，而浏览器和源服务器都没有办法判断报文的真伪。</p>
<p>这对于网络购物、网上银行、证券交易等需要高度信任的应用场景来说是非常致命的。如果没有基本的安全保护，使用互联网进行各种电子商务、电子政务就根本无从谈起。</p>
<p>对于安全性要求不那么高的新闻、视频、搜索等网站来说，由于互联网上的恶意用户、恶意代理越来越多，也很容易遭到“流量劫持”的攻击，在页面里强行嵌入广告，或者分流用户，导致各种利益损失。</p>
<p>对于你我这样的普通网民来说，HTTP 不安全的隐患就更大了，上网的记录会被轻易截获，网站是否真实也无法验证，黑客可以伪装成银行网站，盗取真实姓名、密码、银行卡等敏感信息，威胁人身安全和财产安全。</p>
<p>总的来说，今天的互联网已经不再是早期的“田园牧歌”时代，而是进入了“黑暗森林”状态。上网的时候必须步步为营、处处小心，否则就会被不知道埋伏在哪里的黑客所“猎杀”。</p>
<h2>什么是安全？</h2>
<p>既然 HTTP“不安全”，那什么样的通信过程才是安全的呢？</p>
<p>通常认为，如果通信过程具备了四个特性，就可以认为是“安全”的，这四个特性是：机密性、完整性，身份认证和不可否认。</p>
<p><strong>机密性</strong>（Secrecy/Confidentiality）是指对数据的“保密”，只能由可信的人访问，对其他人是不可见的“秘密”，简单来说就是不能让不相关的人看到不该看的东西。</p>
<p>比如小明和小红私下聊天，但“隔墙有耳”，被小强在旁边的房间里全偷听到了，这就是没有机密性。我们之前一直用的 Wireshark ，实际上也是利用了 HTTP 的这个特点，捕获了传输过程中的所有数据。</p>
<p><strong>完整性</strong>（Integrity，也叫一致性）是指数据在传输过程中没有被窜改，不多也不少，“完完整整”地保持着原状。</p>
<p>机密性虽然可以让数据成为“秘密”，但不能防止黑客对数据的修改，黑客可以替换数据，调整数据的顺序，或者增加、删除部分数据，破坏通信过程。</p>
<p>比如，小明给小红写了张纸条：“明天公园见”。小强把“公园”划掉，模仿小明的笔迹把这句话改成了“明天广场见”。小红收到后无法验证完整性，信以为真，第二天的约会就告吹了。</p>
<p><strong>身份认证</strong>（Authentication）是指确认对方的真实身份，也就是“证明你真的是你”，保证消息只能发送给可信的人。</p>
<p>如果通信时另一方是假冒的网站，那么数据再保密也没有用，黑客完全可以使用冒充的身份“套”出各种信息，加密和没加密一样。</p>
<p>比如，小明给小红写了封情书：“我喜欢你”，但不留心发给了小强。小强将错就错，假冒小红回复了一个“白日做梦”，小明不知道这其实是小强的话，误以为是小红的，后果可想而知。</p>
<p>第四个特性是<strong>不可否认</strong>（Non-repudiation/Undeniable），也叫不可抵赖，意思是不能否认已经发生过的行为，不能“说话不算数”“耍赖皮”。</p>
<p>使用前三个特性，可以解决安全通信的大部分问题，但如果缺了不可否认，那通信的事务真实性就得不到保证，有可能出现“老赖”。</p>
<p>比如，小明借了小红一千元，没写借条，第二天矢口否认，小红也确实拿不出借钱的证据，只能认倒霉。另一种情况是小明借钱后还了小红，但没写收条，小红于是不承认小明还钱的事，说根本没还，要小明再掏出一千元。</p>
<p>所以，只有同时具备了机密性、完整性、身份认证、不可否认这四个特性，通信双方的利益才能有保障，才能算得上是真正的安全。</p>
<h2>什么是 HTTPS？</h2>
<p>说到这里，终于轮到今天的主角 HTTPS 出场了，它为 HTTP 增加了刚才所说的四大安全特性。</p>
<p>HTTPS 其实是一个“非常简单”的协议，RFC 文档很小，只有短短的 7 页，里面规定了<strong>新的协议名“https”，默认端口号 443</strong>，至于其他的什么请求 - 应答模式、报文结构、请求方法、URI、头字段、连接管理等等都完全沿用 HTTP，没有任何新的东西。</p>
<p>也就是说，除了协议名“http”和端口号 80 这两点不同，HTTPS 协议在语法、语义上和 HTTP 完全一样，优缺点也“照单全收”（当然要除去“明文”和“不安全”）。</p>
<p>不信你可以用 URI“<a href="https://www.chrono.com/">https://www.chrono.com</a>”访问之前 08 至 21 讲的所有示例，看看它的响应报文是否与 HTTP 一样。</p>
<pre><code>https://www.chrono.com
https://www.chrono.com/11-1
https://www.chrono.com/15-1?name=a.json
https://www.chrono.com/16-1
</code></pre>
<p><img src="assets/40fbb989a9fd2217320ab287e80e1fb0.png" alt="img" /></p>
<p>你肯定已经注意到了，在用 HTTPS 访问实验环境时 Chrome 会有不安全提示，必须点击“高级 - 继续前往”才能顺利显示页面。而且如果用 Wireshark 抓包，也会发现与 HTTP 不一样，不再是简单可见的明文，多了“Client Hello”“Server Hello”等新的数据包。</p>
<p>这就是 HTTPS 与 HTTP 最大的区别，它能够鉴别危险的网站，并且尽最大可能保证你的上网安全，防御黑客对信息的窃听、窜改或者“钓鱼”、伪造。</p>
<p>你可能要问了，既然没有新东西，HTTPS 凭什么就能做到机密性、完整性这些安全特性呢？</p>
<p>秘密就在于 HTTPS 名字里的“S”，它把 HTTP 下层的传输协议由 TCP/IP 换成了 SSL/TLS，由“<strong>HTTP over TCP/IP</strong>”变成了“<strong>HTTP over SSL/TLS</strong>”，让 HTTP 运行在了安全的 SSL/TLS 协议上（可参考第 4 讲和第 5 讲），收发报文不再使用 Socket API，而是调用专门的安全接口。</p>
<p><img src="assets/50d57e18813e18270747806d5d73f0a3.png" alt="img" /></p>
<p>所以说，HTTPS 本身并没有什么“惊世骇俗”的本事，全是靠着后面的 SSL/TLS“撑腰”。只要学会了 SSL/TLS，HTTPS 自然就“手到擒来”。</p>
<h2>SSL/TLS</h2>
<p>现在我们就来看看 SSL/TLS，它到底是个什么来历。</p>
<p>SSL 即安全套接层（Secure Sockets Layer），在 OSI 模型中处于第 5 层（会话层），由网景公司于 1994 年发明，有 v2 和 v3 两个版本，而 v1 因为有严重的缺陷从未公开过。</p>
<p>SSL 发展到 v3 时已经证明了它自身是一个非常好的安全通信协议，于是互联网工程组 IETF 在 1999 年把它改名为 TLS（传输层安全，Transport Layer Security），正式标准化，版本号从 1.0 重新算起，所以 TLS1.0 实际上就是 SSLv3.1。</p>
<p>到今天 TLS 已经发展出了三个版本，分别是 2006 年的 1.1、2008 年的 1.2 和去年（2018）的 1.3，每个新版本都紧跟密码学的发展和互联网的现状，持续强化安全和性能，已经成为了信息安全领域中的权威标准。</p>
<p>目前应用的最广泛的 TLS 是 1.2，而之前的协议（TLS1.1/1.0、SSLv3/v2）都已经被认为是不安全的，各大浏览器即将在 2020 年左右停止支持，所以接下来的讲解都针对的是 TLS1.2。</p>
<p>TLS 由记录协议、握手协议、警告协议、变更密码规范协议、扩展协议等几个子协议组成，综合使用了对称加密、非对称加密、身份认证等许多密码学前沿技术。</p>
<p>浏览器和服务器在使用 TLS 建立连接时需要选择一组恰当的加密算法来实现安全通信，这些算法的组合被称为“密码套件”（cipher suite，也叫加密套件）。</p>
<p>你可以访问实验环境的 URI“/23-1”，对 TLS 和密码套件有个感性的认识。</p>
<p><img src="assets/5ead57e03f127ea8f244d715186adb24.png" alt="img" /></p>
<p>你可以看到，实验环境使用的 TLS 是 1.2，客户端和服务器都支持非常多的密码套件，而最后协商选定的是“ECDHE-RSA-AES256-GCM-SHA384”。</p>
<p>这么长的名字看着有点晕吧，不用怕，其实 TLS 的密码套件命名非常规范，格式很固定。基本的形式是“密钥交换算法 + 签名算法 + 对称加密算法 + 摘要算法”，比如刚才的密码套件的意思就是：</p>
<p>“握手时使用 ECDHE 算法进行密钥交换，用 RSA 签名和身份认证，握手后的通信使用 AES 对称算法，密钥长度 256 位，分组模式是 GCM，摘要算法 SHA384 用于消息认证和产生随机数。”</p>
<h2>OpenSSL</h2>
<p>说到 TLS，就不能不谈到 OpenSSL，它是一个著名的开源密码学程序库和工具包，几乎支持所有公开的加密算法和协议，已经成为了事实上的标准，许多应用软件都会使用它作为底层库来实现 TLS 功能，包括常用的 Web 服务器 Apache、Nginx 等。</p>
<p>OpenSSL 是从另一个开源库 SSLeay 发展出来的，曾经考虑命名为“OpenTLS”，但当时（1998 年）TLS 还未正式确立，而 SSL 早已广为人知，所以最终使用了“OpenSSL”的名字。</p>
<p>OpenSSL 目前有三个主要的分支，1.0.2 和 1.1.0 都将在今年（2019）年底不再维护，最新的长期支持版本是 1.1.1，我们的实验环境使用的 OpenSSL 是“1.1.0j”。</p>
<p>由于 OpenSSL 是开源的，所以它还有一些代码分支，比如 Google 的 BoringSSL、OpenBSD 的 LibreSSL，这些分支在 OpenSSL 的基础上删除了一些老旧代码，也增加了一些新特性，虽然背后有“大金主”，但离取代 OpenSSL 还差得很远。</p>
<h2>小结</h2>
<ol>
<li>因为 HTTP 是明文传输，所以不安全，容易被黑客窃听或窜改；</li>
<li>通信安全必须同时具备机密性、完整性，身份认证和不可否认这四个特性；</li>
<li>HTTPS 的语法、语义仍然是 HTTP，但把下层的协议由 TCP/IP 换成了 SSL/TLS；</li>
<li>SSL/TLS 是信息安全领域中的权威标准，采用多种先进的加密技术保证通信安全；</li>
<li>OpenSSL 是著名的开源密码学工具包，是 SSL/TLS 的具体实现。</li>
</ol>
<h2>课下作业</h2>
<ol>
<li>你能说出 HTTPS 与 HTTP 有哪些区别吗？</li>
<li>你知道有哪些方法能够实现机密性、完整性等安全特性呢？</li>
</ol>
<p>欢迎你把自己的学习体会写在留言区，与我和其他同学一起讨论。如果你觉得有所收获，也欢迎把文章分享给你的朋友。</p>
<p><img src="assets/052e28eaa90a37f21ae4052135750a4a.png" alt="unpreview" /></p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="22&#32;&#32;冷链周转：HTTP的缓存代理.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="24&#32;&#32;固若金汤的根本（上）：对称加密与非对称加密.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435c5bc863645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
