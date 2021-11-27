<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>08  DDD 是如何解决微服务拆分难题的？.md</title>
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

                    
                    <a href="00&#32;开篇词&#32;&#32;让我们把&#32;DDD&#32;的思想真正落地.md">00 开篇词  让我们把 DDD 的思想真正落地.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;DDD&#32;：杜绝软件退化的利器.md">01  DDD ：杜绝软件退化的利器.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;以电商支付功能为例演练&#32;DDD.md">02  以电商支付功能为例演练 DDD.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;DDD&#32;是如何落地到数据库设计的？.md">03  DDD 是如何落地到数据库设计的？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;领域模型是如何指导程序设计的？.md">04  领域模型是如何指导程序设计的？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;聚合、仓库与工厂：傻傻分不清楚.md">05  聚合、仓库与工厂：傻傻分不清楚.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;限界上下文：冲破微服务设计困局的利器.md">06  限界上下文：冲破微服务设计困局的利器.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;在线订餐场景中是如何开事件风暴会议的？.md">07  在线订餐场景中是如何开事件风暴会议的？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="08&#32;&#32;DDD&#32;是如何解决微服务拆分难题的？.md">08  DDD 是如何解决微服务拆分难题的？.md</a>
                    

                </li>
                <li>

                    
                    <a href="09&#32;&#32;DDD&#32;是如何落地微服务设计实现的？.md">09  DDD 是如何落地微服务设计实现的？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;微服务落地的技术实践.md">10  微服务落地的技术实践.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;解决技术改造困局的钥匙：整洁架构.md">11  解决技术改造困局的钥匙：整洁架构.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;如何设计支持快速交付的技术中台战略？.md">12  如何设计支持快速交付的技术中台战略？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;如何实现支持快速交付的技术中台设计？.md">13  如何实现支持快速交付的技术中台设计？.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;如何设计支持&#32;DDD&#32;的技术中台？.md">14  如何设计支持 DDD 的技术中台？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;如何设计支持微服务的技术中台？.md">15  如何设计支持微服务的技术中台？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;基于&#32;DDD&#32;的代码设计演示（含&#32;DDD&#32;的技术中台设计）.md">16  基于 DDD 的代码设计演示（含 DDD 的技术中台设计）.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;基于&#32;DDD&#32;的微服务设计演示（含支持微服务的&#32;DDD&#32;技术中台设计）.md">17  基于 DDD 的微服务设计演示（含支持微服务的 DDD 技术中台设计）.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;基于事件溯源的设计开发.md">18  基于事件溯源的设计开发.md</a>

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
                        <div><h1>08  DDD 是如何解决微服务拆分难题的？</h1>
<p>微服务的技术架构其实并不难。很多开发团队在微服务转型初期，将关注点主要放到了对微服务技术架构的学习。然而，当他们真正开始将微服务落地到具体的业务中时，才发现，真正的难题是微服务按照什么原则拆分、如何拆分，以及会面对哪些潜在风险。下面我们来一一解决。</p>
<h3>微服务拆分的原则</h3>
<p>在前面的内容中，我们多次提到过微服务的拆分原则，接下来我将为你详细讲解下。</p>
<p><strong>微服务的拆分原则就是“小而专”，即微服务内高内聚、微服务间低耦合。</strong></p>
<p><strong>“微服务内高内聚”</strong>，<strong>就是单一职责原则</strong>，即每个微服务中的代码都是软件变化的一个原因。因这个原因而需要变更的代码都在这个微服务中，与其他微服务无关，那么就可以将代码修改的范围缩小到这个微服务内。把这个微服务修改好了，独立修改、独立发布，该需求就实现了。这样，微服务的优势就发挥出来了。</p>
<p><strong>“微服务间低耦合”</strong>，就是说在微服务实现自身业务的过程中，如果需要执行的某些过程不是自己的职责，就应当将这些过程交给其他微服务去实现，你只需要对它的接口进行调用。譬如，“用户下单”微服务在下单过程中需要查询用户信息，但“查询用户信息”不是它的职责，而是“用户注册”微服务的职责。这样，“用户下单”微服务就不需要再去执行对用户信息的查询，而是直接调用“用户注册”微服务的接口。那么，怎样调用呢？直接调用可能会形成耦合。通过注册中心，“用户下单”微服务调用的只是在注册中心中名称叫“用户注册”的微服务。而在软件设计时，“用户注册”可以有多个实现，哪个注册到注册中心中，就调用哪个。这样，微服务之间的调用就实现了解耦。</p>
<p>通过 DDD 进行业务建模，再基于领域模型进行限界上下文划分，就能保证系统的设计，在限界上下文内高内聚，在限界上下文间低耦合。所以，基于限界上下文进行微服务的拆分，就能保证微服务设计的高质量。同时，通过对上下文地图的分析，就能理清微服务之间的接口调用关系，从而协调多个开发团队协同开发。</p>
<h3>子域划分与限界上下文</h3>
<p>正如第 06 讲中谈到，领域模型的绘制，不是将整个系统的领域对象都绘制在一张大图上，那样绘制很费劲，阅读也很费劲，不利于相互的交流。因此，领域建模就是将一个系统划分成了多个子域，每个子域都是一个独立的业务场景。围绕着这个业务场景进行分析建模，该业务场景会涉及许多领域对象，而这些领域对象又可能与其他子域的对象进行关联。这样，每个子域的实现就是“限界上下文”，而它们之间的关联关系就是“上下文地图”。</p>
<p>在本案例中，围绕着领域事件“已下单”进行分析。它属于“用户下单”这个限界上下文，但与之相关的“用户”及其“地址”来源于“用户注册”这个限界上下文，与之相关的“饭店”及其“菜单”来源于“饭店管理”这个限界上下文。因此，<strong>在这个业务场景中</strong>，“<strong>用户下单</strong>”<strong>限界上下文属于</strong>“<strong>主题域</strong>”，<strong>而</strong>“<strong>用户注册</strong>”<strong>与</strong>“<strong>饭店管理</strong>”<strong>限界上下文属于</strong>“<strong>支撑域</strong>”。同理，围绕着本案例的各个领域事件进行了如下一些设计：</p>
<p><img src="assets/CgqCHl_PFjeATu8NAAC_hYefOkM066.png" alt="Drawing 0.png" /></p>
<p>“已下单”的限界上下文分析图</p>
<p>通过这样的设计，就能将“用户下单”限界上下文的范围，与之相关的上下文地图以及如何接口，分析清楚了。有了这些设计，就可以按照限界上下文进行微服务拆分。按照这样的设计拆分的微服务，所有与用户下单相关的需求变更都在“用户下单”微服务中实现。但是，订单在读取用户信息的时候，不是直接去 join 用户信息表，而是调用“用户注册”微服务的接口。这样，当用户信息发生变更时，与“用户下单”微服务无关，只需要在“用户注册”微服务中独立开发、独立升级，从而使系统维护的成本得到降低。</p>
<p><img src="assets/Ciqc1F_PFkSANv_cAADHnRBTKv4044.png" alt="Drawing 1.png" /></p>
<p>“已接单”与“已就绪”的限界上下文分析图</p>
<p>同样，如上图所示，我们围绕着“已接单”与“已就绪”的限界上下文进行了分析，并将它们都划分到“饭店接单”限界上下文中，后面就会设计成“饭店接单”微服务。这些场景的主题域就是“饭店接单”限界上下文，而与之相关的支撑域就是“用户注册”与“用户下单”限界上下文。通过这些设计，不仅合理划分了微服务的范围，也明确了微服务之间的接口，实现了微服务内的高内聚与微服务间的低耦合。</p>
<h3>领域事件通知机制</h3>
<p>按照 07 讲所讲到的领域模型设计，以及基于该模型的限界上下文划分，将整个系统划分为了“用户下单”“饭店接单”“骑士派送”等微服务。但是，在设计实现的时候，还有一个设计难题，即<strong>领域事件该如何通知</strong>。譬如，当用户在“用户下单”微服务中下单，那么会在该微服务中形成一个订单；但是，“饭店接单”是另外一个微服务，它必须要及时获得已下单的订单信息，才能执行接单。那么，如何通知“饭店接单”微服务已经有新的订单。诚然，可以让“饭店接单”微服务按照一定的周期不断地去查询“用户下单”微服务中已下单的订单信息。然而，这样的设计，不仅会加大“用户下单”与“饭店接单”微服务的系统负载，形成资源的浪费，还会带来这两个微服务之间的耦合，不利于之后的维护。因此，<strong>最有效的方式就是通过消息队列</strong>，<strong>实现领域事件在微服务间的通知</strong>。</p>
<p><img src="assets/CgqCHl_PFlaADZxNAACzNn8_lDg752.png" alt="Drawing 2.png" /></p>
<p><img src="assets/Ciqc1F_PF4OAaM-IAAJp9ADRF8I804.png" alt="Drawing 3.png" /></p>
<p>在线订餐系统的领域事件通知</p>
<p>如上图所示，具体的设计就是，当“用户下单”微服务在完成下单并保存订单以后，将该订单做成一个消息发送到消息队列中；这时，“饭店接单”微服务就会有一个守护进程不断监听消息队列；一旦有消息就会触发接收消息，并向饭店发送“接收订单”的通知。在这样的设计中：</p>
<ul>
<li>“<strong>用户下单</strong>”<strong>微服务只负责发送消息</strong>，至于谁会接收并处理这些消息，与“用户下单”微服务无关；</li>
<li>“<strong>饭店接单</strong>”<strong>微服务只负责接收消息</strong>，至于谁发送的这个消息，与“饭店接单”微服务无关。</li>
</ul>
<p><strong>这样的设计就实现了微服务之间的解耦，使得日后变更的成本降低</strong>。同样，饭店餐食就绪以后，也是通过消息队列通知“骑士接单”。在整个微服务系统中，微服务与微服务之间的领域事件通知会经常存在，所以最好在架构设计中将这个机制下沉到技术中台中。</p>
<h3>DDD 的微服务设计</h3>
<p>通过第 07 讲所讲到的一系列领域驱动设计：</p>
<ul>
<li><strong>首先通过事件风暴会议进行领域建模</strong>；</li>
<li><strong>接着基于领域建模进行限界上下文的设计</strong>。</li>
</ul>
<p>所有这些设计都是为了指导最终微服务的设计。</p>
<p>在 DDD 指导微服务设计的过程中：</p>
<ul>
<li>首先按照限界上下文进行<strong>微服务的拆分</strong>，按照上下文地图定义<strong>各微服务之间的接口与调用关系</strong>；</li>
<li>在此基础上，通过限界上下文的划分，将<strong>领域模型划分到多个问题子域</strong>，每个子域都有一个领域模型的设计；</li>
<li>这样，按照各子域的领域模型，基于充血模型与贫血模型<strong>设计各个微服务的业务领域层</strong>，即各自的 Service、Entity 与 Value Object；</li>
<li>同时，按照领域模型<strong>设计各个微服务的数据库</strong>。</li>
</ul>
<p>最后，将以上的设计最终落实到微服务之间的调用、领域事件的通知，以及前端微服务的设计。如下图所示：</p>
<p><img src="assets/Ciqc1F_PF5aAIjkkAAXZApoF_cg761.png" alt="Drawing 4.png" /></p>
<p>在线订餐系统的微服务设计</p>
<p>这里可以看到，前端微服务与后端微服务的设计是不一致的。前面讲的都是后端微服务的设计，而前端微服务的设计与用户 UI 是密切关联的，因此通过不同角色的规划，将前端微服务划分为用户 App、饭店 Web 与骑士 App。在用户 App 中，所有面对用户的诸如“用户注册”“用户下单”“用户选购”等功能都设计在用户 App 中。它相当于一个聚合服务，用于接收用户请求：</p>
<ul>
<li>“用户注册”时，调用“用户注册”微服务；</li>
<li>“用户选购”时，查询“饭店管理”微服务；</li>
<li>“用户下单”时，调用“用户下单”微服务。</li>
</ul>
<h3>总结</h3>
<p>采用 DDD 进行需求的分析建模，可以帮助微服务的设计质量提高，实现“低耦合、高内聚”，进而充分发挥微服务的优势。然而，在微服务的设计实现还要解决诸多的难题。本讲一一拆解了微服务设计实现的这些难题，及其解决思路。然而，要更加完美地解决以上问题，不是让每个微服务都去见招拆招，而是应当有一个微服务的技术中台统一去解决。这些方面的设计将在后面微服务技术中台建设的相关章节进行讲解。</p>
<p>下一讲我们将演练在以上领域模型与微服务设计的基础上，如何落实每一个微服务的设计，以及可能面临的设计难题。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="07&#32;&#32;在线订餐场景中是如何开事件风暴会议的？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="09&#32;&#32;DDD&#32;是如何落地微服务设计实现的？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433e1dcb3b70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/DDD%20%E5%BE%AE%E6%9C%8D%E5%8A%A1%E8%90%BD%E5%9C%B0%E5%AE%9E%E6%88%98/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
