<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>30 RocketMQ 学习方法之我见.md</title>
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

                    
                    <a href="01&#32;搭建学习环境准备篇.md">01 搭建学习环境准备篇.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;RocketMQ&#32;核心概念扫盲篇.md">02 RocketMQ 核心概念扫盲篇.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;消息发送&#32;API&#32;详解与版本变迁说明.md">03 消息发送 API 详解与版本变迁说明.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;结合实际应用场景谈消息发送.md">04 结合实际应用场景谈消息发送.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;消息发送核心参数与工作原理详解.md">05 消息发送核心参数与工作原理详解.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;消息发送常见错误与解决方案.md">06 消息发送常见错误与解决方案.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;事务消息使用及方案选型思考.md">07 事务消息使用及方案选型思考.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;消息消费&#32;API&#32;与版本变迁说明.md">08 消息消费 API 与版本变迁说明.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;DefaultMQPushConsumer&#32;核心参数与工作原理.md">09 DefaultMQPushConsumer 核心参数与工作原理.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;DefaultMQPushConsumer&#32;使用示例与注意事项.md">10 DefaultMQPushConsumer 使用示例与注意事项.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;DefaultLitePullConsumer&#32;核心参数与实战.md">11 DefaultLitePullConsumer 核心参数与实战.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;结合实际场景再聊&#32;DefaultLitePullConsumer&#32;的使用.md">12 结合实际场景再聊 DefaultLitePullConsumer 的使用.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;结合实际场景顺序消费、消息过滤实战.md">13 结合实际场景顺序消费、消息过滤实战.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;消息消费积压问题排查实战.md">14 消息消费积压问题排查实战.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;RocketMQ&#32;常用命令实战.md">15 RocketMQ 常用命令实战.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;RocketMQ&#32;集群性能摸高.md">16 RocketMQ 集群性能摸高.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;RocketMQ&#32;集群性能调优.md">17 RocketMQ 集群性能调优.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;RocketMQ&#32;集群平滑运维.md">18 RocketMQ 集群平滑运维.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;RocketMQ&#32;集群监控（一）.md">19 RocketMQ 集群监控（一）.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;RocketMQ&#32;集群监控（二）.md">20 RocketMQ 集群监控（二）.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;RocketMQ&#32;集群告警.md">21 RocketMQ 集群告警.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;RocketMQ&#32;集群踩坑记.md">22 RocketMQ 集群踩坑记.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;消息轨迹、ACL&#32;与多副本搭建.md">23 消息轨迹、ACL 与多副本搭建.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;RocketMQ-Console&#32;常用页面指标获取逻辑.md">24 RocketMQ-Console 常用页面指标获取逻辑.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;RocketMQ&#32;Nameserver&#32;背后的设计理念.md">25 RocketMQ Nameserver 背后的设计理念.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;Java&#32;并发编程实战.md">26 Java 并发编程实战.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;从&#32;RocketMQ&#32;学基于文件的编程模式（一）.md">27 从 RocketMQ 学基于文件的编程模式（一）.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;从&#32;RocketMQ&#32;学基于文件的编程模式（二）.md">28 从 RocketMQ 学基于文件的编程模式（二）.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;从&#32;RocketMQ&#32;学&#32;Netty&#32;网络编程技巧.md">29 从 RocketMQ 学 Netty 网络编程技巧.md</a>

                </li>
                <li>

                    <a class="current-tab" href="30&#32;RocketMQ&#32;学习方法之我见.md">30 RocketMQ 学习方法之我见.md</a>
                    

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
                        <div><h1>30 RocketMQ 学习方法之我见</h1>
<p>亲爱的读者朋友，RocketMQ 实战专辑的全部内容即将更新完毕，前面的篇幅主要是介绍 RocketMQ 技术本身，本篇想和大家谈谈我是如何学习 RocketMQ 的，尽量做到授之以渔。</p>
<p>我想大家都会有这样一个共识：<strong>光学理论没用，要实战</strong>。这个有一定的道理，但不应该成为阻碍我们学习的理由。对知识的学习我们当然需要优先学习研究工作中常用的技术，例如以微服务为例，现在市面上 Spring Clould 很火，但公司主要用的是 Dubbo，如果此时你想深入研究微服务，我建议优先选择学习 Dubbo，因为你有实践经验，深入研究 Dubbo 能更好的指导实践，从而实现理论与实际相结合，并且 Dubbo 在市面上也使用的很广泛。</p>
<p>但有时候受到所在平台的限制，日常工作中无法接触到主流的技术，例如缺乏高并发、压根就没有接触过消息中间件，此时该怎么办？</p>
<p><strong>笔者个人的建议</strong>：在无法实际使用时，应该去研究主流技术的原理，为使用做好准备，不要因为没有接触到而放弃学习，机会是留给有准备的人，如果你对某一项技术研究有一定深度时，当项目中需要使用时，你可以立马施展你的才华，很容易脱颖而出。</p>
<p>我在学习 RocketMQ 之前在实际工作中没有接触过任意一款消息中间件，更别谈使用了，促成我学习 RocketMQ 的原因是我得知 RocketMQ 被捐献给 Apache 基金会，而且还听说 RocketMQ 支撑了阿里双十一的具大流量，让我比较好奇，想一睹一款高性能的分布式消息中间件的风采，从此踏上了学习 RocketMQ 的历程。</p>
<p><strong>确定好目标后，该怎么学习 RocketMQ 呢？</strong></p>
<p><strong>1. 通读 RocketMQ 官方设计手册</strong></p>
<p>通常开始学习一个开源框架(产品)，建议大家首先去官网查看其用户手册、设计手册，从而对该框架能解决什么问题，基本的工作原理、涵盖了哪些知识点（后续可以对这些知识点一一突破），从全局上掌握这块中间件。我还清晰的记得我在看 RokcetMQ 设计手册时，我不仅将一些属于理解透彻，并且一些与性能方面的“高级”名词深深的吸引了我，例如：</p>
<ul>
<li>亿级消息堆积能力</li>
<li>内存映射、pagecache</li>
<li>零拷贝</li>
<li>同步刷盘、异步刷盘</li>
<li>同步复制、异步复制</li>
<li>Hash 索引</li>
</ul>
<p>看过设计手册后，让我产生了极大的兴趣，下决心从源码角度对其进行深入研究，立下了不仅深入研究 RocketMQ 的工作原理与实现细节，更是想掌握基于文件编程的设计理念，如何在实践中使用内存映射。</p>
<p><strong>2. 下载源码，跑通 Demo</strong></p>
<p>每一个开源框架，都会提供完备的测试案例，RokcetMQ 也不例外，RokcetMQ 的源码中有一个单独的模块 example，里面放了很多使用 Demo，按需运行一些测试用例，能让你掌握 RokcetMQ 的基本使用，算是入了一个门。</p>
<p><strong>3. 源码研究 RocketMQ</strong></p>
<p>通过前面两个步骤，对设计原理有了一个全局的理解，同时掌握了 RocketMQ 的基本使用，接下来需要深入探究 RocketMQ，特别是如果大家认真阅读了本专栏的所有实战类文章，那是时候研究其源码了。</p>
<p>阅读 RocketMQ 原理个人觉得有如下几个好处：</p>
<ul>
<li>深入研究其实现原理，成体系化的研读 RocketMQ，对 RocketMQ 更具掌控性。通常对应消息中间件，如果出现故障，通常会给公司业务造成较大损失，当出现问题时快速止血固然重要，更难能可贵的时预判风险，避免生产故障发生，要做到预判风险，成体系化研究 RocketMQ 显得非常必要。</li>
<li>学习优秀的 RocketMQ 框架，提升编程技能，例如高并发、基于文件编程相关的技巧，我们都可以从中得到一些启发。</li>
</ul>
<p><strong>那如何阅读 RocketMQ 源码呢？</strong></p>
<p>阅读源码之前还是需要具备一定的基础，建议在阅读 RokcetMQ 源码之前，先尝试阅读一下 Java 数据结构相关的源码，例如 HashMap、ArrayList，主要是培养自己阅读源码的方法，<strong>通常我阅读源码的方法：先主流程、后分支流程</strong>。</p>
<p>我举一个简单的例子来说明先主流程、后分支流程。</p>
<p>例如我在学习消息发送流程时，我只关注消息发送在客户端的流程，至于服务端接收到消息发送请求时，存储、复制、刷盘这些我都暂时不关注，我暂时先关注消息发送在客户端的设计，等弄明白了，后面再去服务端接收消息发送请求时会做哪些操作，然后逐一理解消息存储、消息刷盘、消息同步等机制，这样就能有条理的，逐个破解 RocketMQ 核心设计理念。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="29&#32;从&#32;RocketMQ&#32;学&#32;Netty&#32;网络编程技巧.md">上一页</a>
                        </div>
                        
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434b53afa170ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/RocketMQ%20%E5%AE%9E%E6%88%98%E4%B8%8E%E8%BF%9B%E9%98%B6%EF%BC%88%E5%AE%8C%EF%BC%89/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
