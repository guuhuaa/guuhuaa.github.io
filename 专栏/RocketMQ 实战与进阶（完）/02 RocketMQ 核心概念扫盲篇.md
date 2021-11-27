<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>02 RocketMQ 核心概念扫盲篇.md</title>
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

                    <a class="current-tab" href="02&#32;RocketMQ&#32;核心概念扫盲篇.md">02 RocketMQ 核心概念扫盲篇.md</a>
                    

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

                    
                    <a href="30&#32;RocketMQ&#32;学习方法之我见.md">30 RocketMQ 学习方法之我见.md</a>

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
                        <div><h1>02 RocketMQ 核心概念扫盲篇</h1>
<p>在正式进入 RocketMQ 的学习之前，我觉得有必要梳理一下 RocketMQ 核心概念，为大家学习 RocketMQ 打下牢固的基础。</p>
<h3>RocketMQ 部署架构</h3>
<p><img src="assets/20200726212547918.png" alt="1" /></p>
<p>在 RocketMQ 主要的组件如下。</p>
<p><strong>NameServer</strong></p>
<p>NameServer 集群，Topic 的路由注册中心，为客户端根据 Topic 提供路由服务，从而引导客户端向 Broker 发送消息。NameServer 之间的节点不通信。路由信息在 NameServer 集群中数据一致性采取的最终一致性。</p>
<p><strong>Broker</strong></p>
<p>消息存储服务器，分为两种角色：Master 与 Slave，上图中呈现的就是 2 主 2 从的部署架构，在 RocketMQ 中，主服务承担读写操作，从服务器作为一个备份，当主服务器存在压力时，从服务器可以承担读服务（消息消费）。所有 Broker，包含 Slave 服务器每隔 30s 会向 NameServer 发送心跳包，心跳包中会包含存在在 Broker 上所有的 Topic 的路由信息。</p>
<p><strong>Client</strong></p>
<p>消息客户端，包括 Producer（消息发送者）和 Consumer（消费消费者）。客户端在同一时间只会连接一台 NameServer，只有在连接出现异常时才会向尝试连接另外一台。客户端每隔 30s 向 NameServer 发起 Topic 的路由信息查询。</p>
<blockquote>
<p>温馨提示：NameServer 是在内存中存储 Topic 的路由信息，持久化 Topic 路由信息的地方是在 Broker 中，即 <code>${ROCKETMQ_HOME}/store/config/topics.json</code>。</p>
</blockquote>
<p>在 RocketMQ 4.5.0 版本后引入了多副本机制，即一个复制组（m-s）可以演变为基于 Raft 协议的复制组，复制组内部使用 Raft 协议保证 Broker 节点数据的强一致性，该部署架构在金融行业用的比较多。</p>
<h3>消息订阅模型</h3>
<p>在 RocketMQ 的消息消费模式采用的是发布与订阅模式。</p>
<ul>
<li>Topic：一类消息的集合，消息发送者将一类消息发送到一个主题中，例如订单模块将订单发送到 order_topic 中，而用户登录时，将登录事件发送到 user_login_topic 中。</li>
<li>ConsumerGroup：消息消费组，一个消费单位的“群体”，消费组首先在启动时需要订阅需要消费的 Topic。一个 Topic 可以被多个消费组订阅，同样一个消费组也可以订阅多个主题。一个消费组拥有多个消费者。</li>
</ul>
<p><strong>术语解释起来有点枯燥晦涩，接下来我举例来阐述。</strong></p>
<p>例如我们在开发一个订单系统，其中有一个子系统：order-service-app，在该项目中会创建一个消费组 order_consumer 来订阅 order_topic，并且基于分布式部署，order-service-app 的部署情况如下：</p>
<p><img src="assets/20200726212314196.png" alt="2" /></p>
<p>即 order-service-app 部署了 3 台服务器，每一个 JVM 进程可以看做是消费组 order_consumer 消费组的其中一个消费者。</p>
<h4><strong>消费模式</strong></h4>
<p>那这三个消费者如何来分工来共同消费 order_topic 中的消息呢？</p>
<p>在 RocketMQ 中支持广播模式与集群模式。</p>
<ul>
<li><strong>广播模式</strong>：一个消费组内的所有消费者每一个都会处理 Topic 中的每一条消息，通常用于刷新内存缓存。</li>
<li><strong>集群模式</strong>：一个消费组内的所有消费者共同消费一个 Topic 中的消息，即分工协作，一个消费者消费一部分数据，启动负载均衡。</li>
</ul>
<p>集群模式是非常普遍的模式，符合分布式架构的基本理念，即横向扩容，当前消费者如果无法快速及时处理消息时，可以通过增加消费者的个数横向扩容，快速提高消费能力，及时处理挤压的消息。</p>
<h4><strong>消费队列负载算法与重平衡机制</strong></h4>
<p>那集群模式下，消费者是如何来分配消息的呢？</p>
<p>例如上面实例中 order_topic 有 16 个队列，那一个拥有 3 个消费者的消费组如何来分配队列中。</p>
<p><strong>在 MQ 领域有一个不成文的约定：同一个消费者同一时间可以分配多个队列，但一个队列同一时间只会分配给一个消费者。</strong></p>
<p><strong>RocketMQ 提供了众多的队列负载算法</strong>，其中最常用的两种平均分配算法。</p>
<ul>
<li>AllocateMessageQueueAveragely：平均分配</li>
<li>AllocateMessageQueueAveragelyByCircle：轮流平均分配</li>
</ul>
<p>为了说明这两种分配算法的分配规则，现在对 16 个队列，进行编号，用 q0~q15 表示，消费者用 c0~c2 表示。</p>
<p>AllocateMessageQueueAveragely 分配算法的队列负载机制如下：</p>
<ul>
<li>c0：q0 q1 q2 q3 q4 q5</li>
<li>c1：q6 q7 q8 q9 q10</li>
<li>c2：q11 q12 q13 q14 q15</li>
</ul>
<p>其算法的特点是用总数除以消费者个数，余数按消费者顺序分配给消费者，故 c0 会多分配一个队列，而且队列分配是连续的。</p>
<p>AllocateMessageQueueAveragelyByCircle 分配算法的队列负载机制如下：</p>
<ul>
<li>c0：q0 q3 q6 q9 q12 q15</li>
<li>c1：q1 q4 q7 q10 q13</li>
<li>c2：q2 q5 q8 q11 q14</li>
</ul>
<p>该分配算法的特点就是轮流一个一个分配。</p>
<blockquote>
<p>温馨提示：如果 Topic 的队列个数小于消费者的个数，那有些消费者无法分配到消息。在 RocketMQ 中一个 Topic 的队列数直接决定了最大消费者的个数，但 Topic 队列个数的增加对 RocketMQ 的性能不会产生影响。</p>
</blockquote>
<p>在实际过程中，对主题进行扩容（增加队列个数）或者对消费者进行扩容、缩容是一件非常寻常的事情，那如果新增一个消费者，该消费者消费哪些队列呢？这就涉及到消息消费队列的重新分配，即<strong>消费队列重平衡机制</strong>。</p>
<p>在 RocketMQ 客户端中会每隔 20s 去查询当前 Topic 的所有队列、消费者的个数，运用队列负载算法进行重新分配，然后与上一次的分配结果进行对比，如果发生了变化，则进行队列重新分配；如果没有发生变化，则忽略。</p>
<p>例如采取的分配算法如下图所示，现在增加一个消费者 c3，那队列的分布情况是怎样的呢？</p>
<p><img src="assets/2020072621232327.png" alt="3" /></p>
<p>根据新的分配算法，其队列最终的情况如下：</p>
<ul>
<li>c0：q0 q1 q2 q3</li>
<li>c1：q4 q5 q6 q7</li>
<li>c2：q8 q9 q10 q11</li>
<li>c3：q12 q13 q14 q15</li>
</ul>
<p>上述整个过程无需应用程序干预，由 RocketMQ 完成。大概的做法就是将将原先分配给自己但这次不属于的队列进行丢弃，新分配的队列则创建新的拉取任务。</p>
<h4><strong>消费进度</strong></h4>
<p>消费者消费一条消息后需要记录消费的位置，这样在消费端重启的时候，继续从上一次消费的位点开始进行处理新的消息。在 RocketMQ 中，消息消费位点的存储是以消费组为单位的。</p>
<p><strong>集群模式</strong>下，消息消费进度存储在 Broker 端，<code>${ROCKETMQ_HOME}/store/config/consumerOffset.json</code> 是其具体的存储文件，其中内容截图如下：</p>
<p><img src="assets/20200726212330669.png" alt="4" /></p>
<p>可见消费进度的 Key 为 <a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="ec98839c858fac8f83829f998189ab9e83999c">[email&#160;protected]</a>，然后每一个队列一个偏移量。</p>
<p><strong>广播模式</strong>的消费进度文件存储在用户的主目录，默认文件全路劲名：<code>${USER_HOME}/.rocketmq_offsets</code>。</p>
<h4><strong>消费模型</strong></h4>
<p>RocketMQ 提供了并发消费、顺序消费两种消费模型。</p>
<ul>
<li><strong>并发消费</strong>：对一个队列中消息，每一个消费者内部都会创建一个线程池，对队列中的消息多线程处理，即偏移量大的消息比偏移量小的消息有可能先消费。</li>
<li><strong>顺序消费</strong>：在某一项场景，例如 MySQL binlog 场景，需要消息按顺序进行消费。在 RocketMQ 中提供了基于队列的顺序消费模型，即尽管一个消费组中的消费者会创建一个多线程，但针对同一个 Queue，会加锁。</li>
</ul>
<p>温馨提示：并发消费模型中，消息消费失败默认会重试 16 次，每一次的间隔时间不一样；而顺序消费，如果一条消息消费失败，则会一直消费，直到消费成功。故在顺序消费的使用过程中，应用程序需要区分系统异常、业务异常，如果是不符合业务规则导致的异常，则重试多少次都无法消费成功，这个时候一定要告警机制，及时进行人为干预，否则消费会积压。</p>
<h3>事务消息</h3>
<p>事务消息并不是为了解决分布式事务，而是提供消息发送与业务落库的一致性，其实现原理就是一次分布式事务的具体运用，请看如下示例：</p>
<p><img src="assets/20200726212339249.png" alt="5" /></p>
<p>上述伪代码中，将订单存储关系型数据库中和将消息发送到 MQ 这是两个不同介质的两个操作，如果能保证消息发送、数据库存储这两个操作要么同时成功，要么同时失败，RocketMQ 为了解决该问题引入了<strong>事务消息</strong>。</p>
<blockquote>
<p>温馨提示，本篇主要目的是让大家知晓各个术语的概念，由于事务消息的使用，将在该专栏的后续文章中详细介绍。</p>
</blockquote>
<h3>定时消息</h3>
<p>开源版本的 RocketMQ 目前并不支持任意精度的定时消息。所谓的定时消息就是将消息发送到 Broker，但消费端不会立即消费，而是要到指定延迟时间后才能被消费端消费。</p>
<p>RocketMQ 目前支持指定级别的延迟，其延迟级别如下：</p>
<pre><code>1s 5s 10s 30s 1m 2m 3m 4m 5m 6m 7m 8m 9m 10m 20m 30m 1h 2h

</code></pre>
<h3>消息过滤</h3>
<p>消息过滤是指消费端可以根据某些条件对一个 Topic 中的消息进行过滤，即只消费一个主题下满足过滤条件的消息。</p>
<p>RocketMQ 目前主要的过滤机制是基于 Tag 的过滤与基于消息属性的过滤，基于消息属性的过滤支持 SQL92 表达式，对消息进行过滤。</p>
<h3>小结</h3>
<p>本文的主要目的是介绍 RocketMQ 常见的术语，例如 NameServer、Broker、主题、消费组、消费者、队列负载算法、队列重平衡机制、并发消费、顺序消费、消费进度存储、定时消息、事务消息、消息过滤等基本概念，为后续的实战系列打下坚实基础。</p>
<p>从下一篇开始，将正式开始 RocketMQ 之旅，开始学习消息发送。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="01&#32;搭建学习环境准备篇.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="03&#32;消息发送&#32;API&#32;详解与版本变迁说明.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434aafaa6470ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
