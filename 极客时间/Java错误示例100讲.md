<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../static/favicon.png">
        <title>Java错误示例100讲.md</title>
        <!-- Spectre.css framework -->
        <link rel="stylesheet" href="../static/index.css">
        <!-- theme css & js -->
        <meta name="generator" content="Hexo 4.2.0">
    </head>

<body>

<div class="book-container">
    <div class="book-sidebar">
        <div class="book-brand">
            <a href="../index.html">
                <img src="../static/favicon.png">
                <span>技术文章摘抄</span>
            </a>
        </div>
        <div class="book-menu uncollapsible">
            <ul class="uncollapsible">
                <li><a href="../index.html" class="current-tab">首页</a></li>
            </ul>

            <ul class="uncollapsible">
                <li><a href="../index.html">上一级</a></li>
            </ul>

            <ul class="uncollapsible">
                <li>

                    
                    <a href="Java基础36讲.md">Java基础36讲.md</a>

                </li>
                <li>

                    <a class="current-tab" href="Java错误示例100讲.md">Java错误示例100讲.md</a>
                    

                </li>
                <li>

                    
                    <a href="Linux性能优化.md">Linux性能优化.md</a>

                </li>
                <li>

                    
                    <a href="MySQL实战45讲.md">MySQL实战45讲.md</a>

                </li>
                <li>

                    
                    <a href="从0开始学微服务.md">从0开始学微服务.md</a>

                </li>
                <li>

                    
                    <a href="代码精进之路.md">代码精进之路.md</a>

                </li>
                <li>

                    
                    <a href="持续交付36讲.md">持续交付36讲.md</a>

                </li>
                <li>

                    
                    <a href="程序员进阶攻略.md">程序员进阶攻略.md</a>

                </li>
                <li>

                    
                    <a href="趣谈网络协议.md">趣谈网络协议.md</a>

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
                        <div><h1>Java错误示例100讲</h1>
<h1>00 开篇词 | 业务代码真的会有这么多坑？</h1>
<p>你好，我是朱晔，贝壳金服的资深架构师。我先和你说说我这 15 年的工作经历吧，以加深彼此的了解。前 7 年，我专注于.NET 领域，负责业务项目的同时，也做了很多社区工作。在 CSDN 做版主期间，我因为回答了大量有关.NET 的问题，并把很多问题的答案总结成了博客，获得了 3 次微软 MVP 的称号。后来，我转到了 Java 领域，也从程序员变为了架构师，更关注开源项目和互联网架构设计。在空中网，我整体负责了百万人在线的大型 MMO 网游《激战》技术平台的架构设计，期间和团队开发了许多性能和稳定性都不错的 Java 框架；在饿了么，我负责过日千万订单量的物流平台的开发管理和架构工作，遇到了许多只有高并发下才会出现的问题，积累了大量的架构经验；现在，我在贝壳金服的基础架构团队，负责基础组件、中间件、基础服务开发规划，制定一些流程和规范，带领团队自研 Java 后端开发框架、微服务治理平台等，在落地 Spring Cloud 结合 Kubernetes 容器云平台技术体系的过程中，摸索出了很多适合公司项目的基础组件和最佳实践。这 15 年来，我一直没有脱离编码工作，接触过大大小小的项目不下 400 个，自己亲身经历的、见别人踩过的坑不计其数。我感触很深的一点是，业务代码中真的有太多的坑：有些是看似非常简单的知识点反而容易屡次踩坑，比如 Spring 声明式事务不生效的问题；而有些坑因为“潜伏期”长，引发的线上事故造成了大量的人力和资金损失。因此，我系统梳理了这些案例和坑点，最终筛选出 100 个案例，涉及 130 多个坑点，组成了这个课程。意识不到业务代码的坑，很危险我想看到 100、130 这两个数字，你不禁要问了：“我写了好几年的业务代码了，遇到问题时上网搜一下就有答案，遇到最多的问题就是服务器不稳定，重启一下基本就可以解决，哪里会有这么多坑呢？”带着这个问题，你继续听我往下说吧。据我观察，很多开发同学没意识到这些坑，有以下三种可能：意识不到坑的存在，比如所谓的服务器不稳定很可能是代码问题导致的，很多时候遇到 OOM、死锁、超时问题在运维层面通过改配置、重启、扩容等手段解决了，没有反推到开发层面去寻找根本原因。有些问题只会在特定情况下暴露。比如，缓存击穿、在多线程环境使用非线程安全的类，只有在多线程或高并发的情况才会暴露问题。有些性能问题不会导致明显的 Bug，只</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="Java基础36讲.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="Linux性能优化.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4364e27ca4645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E6%9E%81%E5%AE%A2%E6%97%B6%E9%97%B4/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
