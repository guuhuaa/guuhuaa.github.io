<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>01  开篇： Kubernetes 是什么以及为什么需要它.md</title>
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

                    <a class="current-tab" href="01&#32;&#32;开篇：&#32;Kubernetes&#32;是什么以及为什么需要它.md">01  开篇： Kubernetes 是什么以及为什么需要它.md</a>
                    

                </li>
                <li>

                    
                    <a href="02&#32;初步认识：Kubernetes&#32;基础概念.md">02 初步认识：Kubernetes 基础概念.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;宏观认识：整体架构.md">03 宏观认识：整体架构.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;搭建&#32;Kubernetes&#32;集群&#32;-&#32;本地快速搭建.md">04 搭建 Kubernetes 集群 - 本地快速搭建.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;动手实践：搭建一个&#32;Kubernetes&#32;集群&#32;-&#32;生产可用.md">05 动手实践：搭建一个 Kubernetes 集群 - 生产可用.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;集群管理：初识&#32;kubectl.md">06 集群管理：初识 kubectl.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;集群管理：以&#32;Redis&#32;为例-部署及访问.md">07 集群管理：以 Redis 为例-部署及访问.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;安全重点&#32;认证和授权.md">08 安全重点 认证和授权.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;应用发布：部署实际项目.md">09 应用发布：部署实际项目.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;应用管理：初识&#32;Helm.md">10 应用管理：初识 Helm.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;部署实践：以&#32;Helm&#32;部署项目.md">11 部署实践：以 Helm 部署项目.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;庖丁解牛：kube-apiserver.md">12 庖丁解牛：kube-apiserver.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;庖丁解牛：etcd.md">13 庖丁解牛：etcd.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;庖丁解牛：controller-manager.md">14 庖丁解牛：controller-manager.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;庖丁解牛：kube-scheduler.md">15 庖丁解牛：kube-scheduler.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;庖丁解牛：kubelet.md">16 庖丁解牛：kubelet.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;庖丁解牛：kube-proxy.md">17 庖丁解牛：kube-proxy.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;庖丁解牛：Container&#32;Runtime&#32;（Docker）.md">18  庖丁解牛：Container Runtime （Docker）.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;Troubleshoot.md">19 Troubleshoot.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;扩展增强：Dashboard.md">20 扩展增强：Dashboard.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;扩展增强：CoreDNS.md">21 扩展增强：CoreDNS.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;服务增强：Ingress.md">22 服务增强：Ingress.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;监控实践：对&#32;K8S&#32;集群进行监控.md">23 监控实践：对 K8S 集群进行监控.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;总结.md">24 总结.md</a>

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
                        <div><h1>01  开篇： Kubernetes 是什么以及为什么需要它</h1>
<p>Kubernetes 是一个可扩展的，用于容器化应用程序编排，管理的平台。由 Google 于 2014 年基于其大规模生产实践经验而开源出来的。Kubernetes 目前在容器编排领域已经成为事实上的标准，社区也非常活跃。</p>
<p>Kubernetes 在国内外都已经得到广泛的应用，无论是Google, Amazon, GitHub 等还是国内的阿里，腾讯，百度，华为，京东或其他中小公司等也都已全力推进 Kubernetes 在生产中的使用。</p>
<p>现在无论是运维，后端，DBA，亦或者是前端，机器学习工程师等都需要在工作中或多或少的用到 Docker， 而在生产中大量使用的话 Kubernetes 也将会成为趋势，所以了解或掌握 Kubernetes 也成为了工程师必不可少的技能之一。</p>
<h2>Kubernetes 是什么?</h2>
<p>当提到 Kubernetes 的时候，大多数人的可能会想到它可以容器编排，想到它是 PaaS (Platform as a Service) 系统，但其实不然，Kubernetes 并不是 PasS 系统，因为它工作在容器层而不是硬件层，它只不过提供了一些与 PasS 类似或者共同的功能，类似部署，扩容，监控，负载均衡，日志记录等。然而它并不是个完全一体化的平台，这些功能基本都是可选可配置的。</p>
<p>Kubernetes 可支持公有云，私有云及混合云等，具备良好的可移植性。我们可直接使用它或在其之上构建自己的容器/云平台，以达到快速部署，快速扩展，及优化资源使用等。</p>
<p>它致力于提供通用接口类似 CNI( Container Network Interface ), CSI（Container Storage Interface）, CRI（Container Runtime Interface）等规范，以便有更多可能, 让更多的厂商共同加入其生态体系内。它的目标是希望在以后，任何团队都可以在不修改 Kubernetes 核心代码的前提下，可以方便的扩展和构建符合自己需求的平台。</p>
<h2>为什么需要 Kubernetes</h2>
<p>我们回到实际的工作环境中。</p>
<ul>
<li>如果你是个前端，你是否遇到过 npm 依赖安装极慢，或是 node sass 安装不了或者版本不对的情况？</li>
<li>如果你是个后端，是否遇到过服务器与本地环境不一致的情况，导致部分功能出现非预期的情况？</li>
<li>如果你是个运维，是否遇到过频繁部署环境，但中间可能出现各种安装不了或者版本不对的问题？</li>
</ul>
<p>目前来看，对于这些问题，最好的解决方案便是标准化，容器化，现在用到最多的也就是 Docker。 Docker 通过 Dockerfile 来对环境进行描述，通过镜像进行交付，使用时不再需要关注环境不一致相关的问题。</p>
<p>现在面试的时候，无论前后端，我们总会多问下是否了解或者使用过 Docker 。如果使用过，那自然会问如果规模变大或者在生产中如何进行容器编排，部署扩容机制如何。</p>
<p>多数人在这个时候都已经回答不上来了，一方面是因为非运维相关岗位的同学，可能在实际工作中并不了解整体的架构体系，没有相关的知识积累。另一方面，对于运维同学可能尚未接触到这部分。</p>
<p>作为一个技术人员，我们应该对整体的体系架构有所了解, 掌握更多的技能，了解软件的完整生命周期，包括开发，交付，部署，以及当流量变大时的扩容等。</p>
<p>在容器编排领域，比较著名的主要有三个：Kubernetes, Mesos, 及 Docker 自家的 Swarm . 对这三者而言，较为简单的是 Swarm, 因为它本身只专注于容器编排，并且是官方团队所作，从各方面来看，对于新手都相对友好一些。但如果是用于生产中大规模使用，反而就略有不及。</p>
<p>而 Mesos 也并不仅限于容器编排，它的创建本身是为了将数据中心的所有资源进行抽象，比如 CPU，内存，网络，存储等，将整个 Mesos 集群当作是一个大的资源池，允许各种 Framework 来进行调度。比如，可以使用 Marathon 来实现 PaaS，可以运行 Spark，Hadoop 等进行计算等。同时因为它支持比如 Docker 或者 LXC 等作资源隔离，所以前几年也被大量用于容器编排。</p>
<p>随着 Kubernetes 在目前的认可度已经超过 Mesos， Docker Swarm 等，无疑它是生产环境中容器应用管理的不二之选。</p>
<p>本小册的目标是帮助更多开发者（不局限于运维，后端，前端等）认识并掌握 Kubernetes 的基础技能，了解其基础架构等。但是 Kubernetes 涉及知识点很多，且更新迭代很快，本小册集中于使用轻快的文字帮助大家掌握 K8S 的通用基础技能，对于其中需掌握的关于 Docker，及 Linux 内核相关的知识不会过于深入解释。主要以最常见 case 入手，帮助大家更快的掌握相关知识并将其用于生产实践中。</p>
</div>
                    </div>
                    <div>
                        
                        <div style="float: right">
                            <a href="02&#32;初步认识：Kubernetes&#32;基础概念.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4345c63ce770ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Kubernetes%20%E4%BB%8E%E4%B8%8A%E6%89%8B%E5%88%B0%E5%AE%9E%E8%B7%B5/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
