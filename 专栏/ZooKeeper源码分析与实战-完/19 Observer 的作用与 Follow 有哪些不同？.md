<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>19 Observer 的作用与 Follow 有哪些不同？.md</title>
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

                    
                    <a href="00&#32;开篇词：选择&#32;ZooKeeper，一步到位掌握分布式开发.md">00 开篇词：选择 ZooKeeper，一步到位掌握分布式开发.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;ZooKeeper&#32;数据模型：节点的特性与应用.md">01 ZooKeeper 数据模型：节点的特性与应用.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;发布订阅模式：如何使用&#32;Watch&#32;机制实现分布式通知.md">02 发布订阅模式：如何使用 Watch 机制实现分布式通知.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;ACL&#32;权限控制：如何避免未经授权的访问？.md">03 ACL 权限控制：如何避免未经授权的访问？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;ZooKeeper&#32;如何进行序列化？.md">04 ZooKeeper 如何进行序列化？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;深入分析&#32;Jute&#32;的底层实现原理.md">05 深入分析 Jute 的底层实现原理.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;ZooKeeper&#32;的网络通信协议详解.md">06 ZooKeeper 的网络通信协议详解.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;单机模式：服务器如何从初始化到对外提供服务？.md">07 单机模式：服务器如何从初始化到对外提供服务？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;集群模式：服务器如何从初始化到对外提供服务？.md">08 集群模式：服务器如何从初始化到对外提供服务？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;创建会话：避开日常开发的那些“坑”.md">09 创建会话：避开日常开发的那些“坑”.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;ClientCnxn：客户端核心工作类工作原理解析.md">10 ClientCnxn：客户端核心工作类工作原理解析.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;分桶策略：如何实现高效的会话管理？.md">11 分桶策略：如何实现高效的会话管理？.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;服务端是如何处理一次会话请求的？.md">12 服务端是如何处理一次会话请求的？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;Curator：如何降低&#32;ZooKeeper&#32;使用的复杂性？.md">13 Curator：如何降低 ZooKeeper 使用的复杂性？.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;Leader&#32;选举：如何保证分布式数据的一致性？.md">14 Leader 选举：如何保证分布式数据的一致性？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;ZooKeeper&#32;究竟是怎么选中&#32;Leader&#32;的？.md">15 ZooKeeper 究竟是怎么选中 Leader 的？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;ZooKeeper&#32;集群中&#32;Leader&#32;与&#32;Follower&#32;的数据同步策略.md">16 ZooKeeper 集群中 Leader 与 Follower 的数据同步策略.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;集群中&#32;Leader&#32;的作用：事务的请求处理与调度分析.md">17 集群中 Leader 的作用：事务的请求处理与调度分析.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;集群中&#32;Follow&#32;的作用：非事务请求的处理与&#32;Leader&#32;的选举分析.md">18 集群中 Follow 的作用：非事务请求的处理与 Leader 的选举分析.md</a>

                </li>
                <li>

                    <a class="current-tab" href="19&#32;Observer&#32;的作用与&#32;Follow&#32;有哪些不同？.md">19 Observer 的作用与 Follow 有哪些不同？.md</a>
                    

                </li>
                <li>

                    
                    <a href="20&#32;一个运行中的&#32;ZooKeeper&#32;服务会产生哪些数据和文件？.md">20 一个运行中的 ZooKeeper 服务会产生哪些数据和文件？.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;ZooKeeper&#32;分布式锁：实现和原理解析.md">21 ZooKeeper 分布式锁：实现和原理解析.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;基于&#32;ZooKeeper&#32;命名服务的应用：分布式&#32;ID&#32;生成器.md">22 基于 ZooKeeper 命名服务的应用：分布式 ID 生成器.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;使用&#32;ZooKeeper&#32;实现负载均衡服务器功能.md">23 使用 ZooKeeper 实现负载均衡服务器功能.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;ZooKeeper&#32;在&#32;Kafka&#32;和&#32;Dubbo&#32;中的工业级实现案例分析.md">24 ZooKeeper 在 Kafka 和 Dubbo 中的工业级实现案例分析.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;如何搭建一个高可用的&#32;ZooKeeper&#32;生产环境？.md">25 如何搭建一个高可用的 ZooKeeper 生产环境？.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;JConsole&#32;与四字母命令：如何监控服务器上&#32;ZooKeeper&#32;的运行状态？.md">26 JConsole 与四字母命令：如何监控服务器上 ZooKeeper 的运行状态？.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;crontab&#32;与&#32;PurgeTxnLog：线上系统日志清理的最佳时间和方式.md">27 crontab 与 PurgeTxnLog：线上系统日志清理的最佳时间和方式.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;彻底掌握二阶段提交三阶段提交算法原理.md">28 彻底掌握二阶段提交三阶段提交算法原理.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;ZAB&#32;协议算法：崩溃恢复和消息广播.md">29 ZAB 协议算法：崩溃恢复和消息广播.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;ZAB&#32;与&#32;Paxos&#32;算法的联系与区别.md">30 ZAB 与 Paxos 算法的联系与区别.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;ZooKeeper&#32;中二阶段提交算法的实现分析.md">31 ZooKeeper 中二阶段提交算法的实现分析.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;ZooKeeper&#32;数据存储底层实现解析.md">32 ZooKeeper 数据存储底层实现解析.md</a>

                </li>
                <li>

                    
                    <a href="33&#32;结束语&#32;&#32;分布技术发展与&#32;ZooKeeper&#32;应用前景.md">33 结束语  分布技术发展与 ZooKeeper 应用前景.md</a>

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
                        <div><h1>19 Observer 的作用与 Follow 有哪些不同？</h1>
<p>在上个课时中，我们学习了 ZooKeeper 集群中 Follow 服务器的作用。在 ZooKeeper 集群服务运行的过程中，Follow 服务器主要负责处理来自客户端的非事务性请求，其中大部分是处理客户端发起的查询会话等请求。而在 ZooKeeper 集群中，Leader 服务器失效时，会在 Follow 集群服务器之间发起投票，最终选举出一个 Follow 服务器作为新的 Leader 服务器。</p>
<p>除了 Leader 和 Follow 服务器，ZooKeeper 集群中还有一个 Observer 服务器。在 ZooKeeper 集群中，Observer 服务器对于提升整个 ZooKeeper 集群运行的性能具有至关重要的作用。而本课时，我们就开始学习什么是 Observer 服务器，以及它在 ZooKeeper 集群中都做了哪些工作。</p>
<h3>Observer 介绍</h3>
<p>在 ZooKeeper 集群服务运行的过程中，Observer 服务器与 Follow 服务器具有一个相同的功能，那就是负责处理来自客户端的诸如查询数据节点等非事务性的会话请求操作。但与 Follow 服务器不同的是，<strong>Observer 不参与 Leader 服务器的选举工作，也不会被选举为 Leader 服务器</strong>。</p>
<p>在前面的课程中，我们或多或少有涉及 Observer 服务器，当时我们把 Follow 服务器和 Observer 服务器统称为 Learner 服务器。你可能会觉得疑惑，Observer 服务器做的事情几乎和 Follow 服务器一样，那么为什么 ZooKeeper 还要创建一个 Observer 角色服务器呢？</p>
<p>要想解释这个问题，就要从 ZooKeeper 技术的发展过程说起，最早的 ZooKeeper 框架如下图所示，可以看到，其中是不存在 Observer 服务器的。</p>
<p><img src="assets/Ciqc1F8FnKWAQEJJAADU9xFvIIU685.png" alt="image" /></p>
<p>在早期的 ZooKeeper 集群服务运行过程中，只有 Leader 服务器和 Follow 服务器。不过随着 ZooKeeper 在分布式环境下的广泛应用，早期模式的设计缺点也随之产生，主要带来的问题有如下几点：</p>
<ol>
<li>随着集群规模的变大，集群处理写入的性能反而下降。</li>
<li>ZooKeeper 集群无法做到跨域部署</li>
</ol>
<p>其中最主要的问题在于，当 ZooKeeper 集群的规模变大，集群中 Follow 服务器数量逐渐增多的时候，ZooKeeper 处理创建数据节点等事务性请求操作的性能就会逐渐下降。这是因为 ZooKeeper 集群在处理事务性请求操作时，要在 ZooKeeper 集群中对该事务性的请求发起投票，只有超过半数的 Follow 服务器投票一致，才会执行该条写入操作。</p>
<p>正因如此，随着集群中 Follow 服务器的数量越来越多，一次写入等相关操作的投票也就变得越来越复杂，并且 Follow 服务器之间彼此的网络通信也变得越来越耗时，导致随着 Follow 服务器数量的逐步增加，事务性的处理性能反而变得越来越低。</p>
<p>为了解决这一问题，在 ZooKeeper 3.6 版本后，ZooKeeper 集群中创建了一种新的服务器角色，即 Observer——观察者角色服务器。Observer 可以处理 ZooKeeper 集群中的非事务性请求，并且不参与 Leader 节点等投票相关的操作。这样既保证了 ZooKeeper 集群性能的扩展性，又避免了因为过多的服务器参与投票相关的操作而影响 ZooKeeper 集群处理事务性会话请求的能力。</p>
<p>在引入 Observer 角色服务器后，一个 ZooKeeper 集群服务在部署的拓扑结构，如下图所示：</p>
<p><img src="assets/Ciqc1F8FnLGAKhD0AAE5oGBLTTQ439.png" alt="image" /></p>
<p>在实际部署的时候，因为 Observer 不参与 Leader 节点等操作，并不会像 Follow 服务器那样频繁的与 Leader 服务器进行通信。因此，可以将 Observer 服务器部署在不同的网络区间中，这样也不会影响整个 ZooKeeper 集群的性能，也就是所谓的跨域部署。</p>
<h3>底层实现</h3>
<p>介绍完 Observer 的作用和原理后，接下来我们再从底层代码的角度去分析一下 ZooKeeper 是如何实现一个 Observer 服务器的。</p>
<p>首先，在我们平时开发 ZooKeeper 服务的时候，如果想让某个服务器以 Observer 角色运行，需要在该服务器的运行配置文件 zoo.cfg 文件中添加 peerType 属性。如下面的代码所示，将该服务器的 peerType 属性设置为 observer 。</p>
<pre><code>peerType=observer 
</code></pre>
<p>而当 ZooKeeper 集群服务开始运行的时候，首先调用 ObserverZooKeeperServer 类，来实例化 ZooKeeper 集群中每个 Observer 服务器，并初始化调用链等相关操作。如下面的代码所示：</p>
<pre><code>ObserverZooKeeperServer(FileTxnSnapLog logFactory, QuorumPeer self, ZKDatabase zkDb) throws IOException {

    super(logFactory, self.tickTime, self.minSessionTimeout, self.maxSessionTimeout, zkDb, self);

    LOG.info(&quot;syncEnabled =&quot; + syncRequestProcessorEnabled);
</code></pre>
<p>而在 ObserverZooKeeperServer 类的 commitRequest 函数中，就设置了与 Follow 角色不同的实现方式。如下面的代码所示，Observer 不会接收网络中的 Proposal 请求，不会像 Follow 一样，在 Proposal 阶段就获得 Leader 服务器发送的变更数据。Observer 服务器是从 INFORM 数据包中获得变更的数据，在 commitRequest 函数的内部实现中，提交执行来自 INFORM 数据包中的事务操作。</p>
<pre><code>public void commitRequest(Request request) {     

    if (syncRequestProcessorEnabled) {

        // Write to txnlog and take periodic snapshot

        syncProcessor.processRequest(request);

    }

    commitProcessor.commit(request);        
</code></pre>
<h3>INFORM 消息</h3>
<p>了解 Observer 服务器的底层实现过程后，我们再来介绍一下 INFORM 消息。Observer 不会接收来自 Leader 服务器提交的投票请求，且不会接收网络中的 Proposal 请求信息，只会从网络中接收 INFORM 类型的信息包。</p>
<p>而 INFORM 信息的内部只包含已经被 Cmmit 操作过的投票信息，因为 Observer 服务器只接收已经被提交处理的 Proposal 请求，不会接收未被提交的会话请求。这样就从底层信息的角度隔离了 Observer 参与投票操作，进而使 Observer 只负责查询等相关非事务性操作，保证扩展多个 Observer 服务器时不会对 ZooKeeper 集群写入操作的性能产生影响。</p>
<h3>Observer 处理链</h3>
<p>接下来，我们再来看一下 Observer 服务器处理一次会话请求的底层实现过程。与 Leader 和 Follow 服务器一样，在处理一条来自客户单的会话请求时， Observer 同样采用的是处理链的设计方式。在这个 Observer 处理链上，主要定义了三个处理器，处理器的执行顺序分别是 ObserverRequestProcessor 处理器、CommitProcessor 处理器以及 FinalRequestProcessor 处理器。</p>
<p>在 ObserverRequestProcessor 处理器中，首先判断客户端请求的会话类型，将所有事务性的会话请求交给 Leader 服务器处理，如下面的代码所示。</p>
<pre><code>public void run() {

        try {

            while (!finished) {

                Request request = queuedRequests.take();

               	...

                switch (request.type) {

                case OpCode.sync:

                    zks.pendingSyncs.add(request);

                    zks.getObserver().request(request);

                    break;

                case OpCode.create:

                case OpCode.create2:

                case OpCode.createTTL:

                case OpCode.createContainer:

                case OpCode.delete:

                case OpCode.deleteContainer:

                case OpCode.setData:

                case OpCode.reconfig:

                case OpCode.setACL:

                case OpCode.multi:

                case OpCode.check:

                    zks.getObserver().request(request);

                    break;

               	...

            }

        } 

        ...

    }

}
</code></pre>
<p>之后调用 CommitProcessor 处理器，将该条会话放入到 queuedRequests 请求等待队列中。并唤醒相关线程进行会话处理。queuedRequests 队列实现了 BlockingQueue 阻塞队列：<strong>当 queuedRequests 队列容器已满，生产者线程会被阻塞，直到队列未满；当队列容器为空时，消费者线程会被阻塞，直至队列非空时为止。</strong> 这就形成了一个消费者—生产者模式的处理方式。</p>
<pre><code>public void processRequest(Request request) {

    if (stopped) {

        return;

    }

    if (LOG.isDebugEnabled()) {

        LOG.debug(&quot;Processing request:: &quot; + request);

    }

    queuedRequests.add(request);

    wakeup();

}
</code></pre>
<p>在将会话请求放入到等待处理队列后，CommitProcessor 处理器的 run 方法从该队列中取出要处理的会话请求，然后解析会话请求中的请求服务器 zxid、请求事务信息 txn、请求头信息 hdr 等，并封装成 requeset 对象，然后传递给下一个处理器 FinalRequestProcessor。FinalRequestProcessor 处理器中会根据请求的类型，最终执行相关的操作。</p>
<h3>结束</h3>
<p>本课时我们学习了在 ZooKeeper 集群服务运行过程中 Observer 服务器的作用和功能。</p>
<p>与 Follow 服务器一样，他们都可以处理 ZooKeeper 集群中的非事务性会话请求，不同之处在于，Observer 不参与 ZooKeeper 集群中 Leader 服务器的选举以及事务性会话处理的投票工作。</p>
<p>这里给你留一个思考题：利用 Observer 服务器的这一特性，在平时的生产环境中，我们可以采用什么样的方式，来提高 ZooKeeper 集群服务的性能呢？所谓的跨域部署最常见的就是将 ZooKeeper 集群中的物理机器部署在不同的地域或机房中。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="18&#32;集群中&#32;Follow&#32;的作用：非事务请求的处理与&#32;Leader&#32;的选举分析.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="20&#32;一个运行中的&#32;ZooKeeper&#32;服务会产生哪些数据和文件？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434ef25a0a70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/ZooKeeper%E6%BA%90%E7%A0%81%E5%88%86%E6%9E%90%E4%B8%8E%E5%AE%9E%E6%88%98-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
