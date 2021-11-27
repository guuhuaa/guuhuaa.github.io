<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>16 RocketMQ 集群性能摸高.md</title>
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

                    <a class="current-tab" href="16&#32;RocketMQ&#32;集群性能摸高.md">16 RocketMQ 集群性能摸高.md</a>
                    

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
                        <div><h1>16 RocketMQ 集群性能摸高</h1>
<h3>前言</h3>
<p>我们在生产环境搭建一个集群时，需要对该集群的性能进行摸高。即：集群的最大 TPS 大约多少，我们做到心里有数。通常我们日常的实际流量控制在压测最高值的 1/3 到 1/2 左右，预留一倍到两倍的空间应对流量的突增情况。</p>
<p>如何进行压力测试呢？</p>
<ol>
<li>写段发送代码测试同学通过 JMeter 进行压力测试，或者代码中通过多线程发送消息。这种方式需要多台不错配置的测试机器。</li>
<li>通过 RocketMQ 自带压测脚本。</li>
</ol>
<p>这两种在实践过程中都使用过，压测效果基本接近，为了方便，建议直接在新搭建的 RocketMQ 集群上直接通过压测脚本进行即可。</p>
<h3>压测脚本</h3>
<p>在 RocketMQ 安装包解压后，在 benchmark 目录有一个 producer.sh 文件。我们通过该脚本进行压力测试。</p>
<p>下面通过 <code>producer.sh -h</code> 看下各个字段的含义。</p>
<p>字段含义：</p>
<table>
<thead>
<tr>
<th align="left">名称</th>
<th align="left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">-h</td>
<td align="left">使用帮助</td>
</tr>
<tr>
<td align="left">-k</td>
<td align="left">测试时消息是否有 key，默认 false</td>
</tr>
<tr>
<td align="left">-n</td>
<td align="left">NameServer 地址</td>
</tr>
<tr>
<td align="left">-s</td>
<td align="left">消息大小，默认为 128 个字节</td>
</tr>
<tr>
<td align="left">-t</td>
<td align="left">主题名称</td>
</tr>
<tr>
<td align="left">-w</td>
<td align="left">并发线程的数量，默认 64 个</td>
</tr>
</tbody>
</table>
<h3>摸高实战</h3>
<p>系统配置 48C256G，集群架构为 4 主 4 从。下面分场景对该集群进行测试，观察输出结果。可以根据实际情况灵活组合，不同的组合结果也不会相同，然而压测的方法是一样的。</p>
<h4><strong>测试场景一</strong></h4>
<p>1 个线程、消息大小为 1K、主题为 8 个队列。以下结果中发送最大 TPS 为 4533，最大 RT 为 299，平均 RT 为 0.22。</p>
<pre><code>sh producer.sh -t cluster-perf-tst8 -w 1 -s 1024 -n x.x.x.x:9876
Send TPS: 4281 Max RT: 299 Average RT:   0.233 Send Failed: 0 Response Failed: 0
Send TPS: 4237 Max RT: 299 Average RT:   0.236 Send Failed: 0 Response Failed: 0
Send TPS: 4533 Max RT: 299 Average RT:   0.221 Send Failed: 0 Response Failed: 0
Send TPS: 4404 Max RT: 299 Average RT:   0.227 Send Failed: 0 Response Failed: 0
Send TPS: 4360 Max RT: 299 Average RT:   0.229 Send Failed: 0 Response Failed: 0
Send TPS: 4269 Max RT: 299 Average RT:   0.234 Send Failed: 0 Response Failed: 0
Send TPS: 4319 Max RT: 299 Average RT:   0.231 Send Failed: 0 Response Failed: 0
</code></pre>
<h4><strong>测试场景二</strong></h4>
<p>1 个线程、消息大小为 3K、主题为 8 个队列。以下结果中发送最大 TPS 为 4125，最大 RT 为 255，平均 RT 为 0.24。</p>
<pre><code>sh producer.sh -t cluster-perf-tst8 -w 1 -s 3072 -n 192.168.x.x:9876
Send TPS: 4120 Max RT: 255 Average RT:   0.242 Send Failed: 0 Response Failed: 0
Send TPS: 4054 Max RT: 255 Average RT:   0.246 Send Failed: 0 Response Failed: 0
Send TPS: 4010 Max RT: 255 Average RT:   0.249 Send Failed: 0 Response Failed: 0
Send TPS: 4125 Max RT: 255 Average RT:   0.242 Send Failed: 0 Response Failed: 0
Send TPS: 4093 Max RT: 255 Average RT:   0.244 Send Failed: 0 Response Failed: 0
Send TPS: 4093 Max RT: 255 Average RT:   0.244 Send Failed: 0 Response Failed: 0
Send TPS: 3999 Max RT: 255 Average RT:   0.250 Send Failed: 0 Response Failed: 0
Send TPS: 3957 Max RT: 255 Average RT:   0.253 Send Failed: 0 Response Failed: 0

</code></pre>
<h4><strong>测试场景三</strong></h4>
<p>1 个线程、消息大小为 1K、主题为 16 个队列。以下结果中发送最大 TPS 为 5289，最大 RT 为 255，平均 RT 为 0.19。</p>
<pre><code>sh producer.sh -t cluster-perf-tst16 -w 1 -s 1024 -n x.x.x.x:9876
Send TPS: 5289 Max RT: 225 Average RT:   0.189 Send Failed: 0 Response Failed: 0
Send TPS: 5252 Max RT: 225 Average RT:   0.190 Send Failed: 0 Response Failed: 0
Send TPS: 5124 Max RT: 225 Average RT:   0.195 Send Failed: 0 Response Failed: 0
Send TPS: 5146 Max RT: 225 Average RT:   0.194 Send Failed: 0 Response Failed: 0
Send TPS: 4861 Max RT: 225 Average RT:   0.206 Send Failed: 0 Response Failed: 0
Send TPS: 4998 Max RT: 225 Average RT:   0.200 Send Failed: 0 Response Failed: 0
Send TPS: 5063 Max RT: 225 Average RT:   0.198 Send Failed: 0 Response Failed: 0
Send TPS: 5039 Max RT: 225 Average RT:   0.198 Send Failed: 0 Response Failed: 0

</code></pre>
<h4><strong>测试场景四</strong></h4>
<p>1 个线程、消息大小为 3K、主题为 16 个队列。以下结果中发送最大 TPS 为 5011，最大 RT 为 244，平均 RT 为 0.21。</p>
<pre><code>sh producer.sh -t cluster-perf-tst16 -w 1 -s 3072 -n x.x.x.x:9876
Send TPS: 4778 Max RT: 244 Average RT:   0.209 Send Failed: 0 Response Failed: 0
Send TPS: 5011 Max RT: 244 Average RT:   0.199 Send Failed: 0 Response Failed: 0
Send TPS: 4826 Max RT: 244 Average RT:   0.207 Send Failed: 0 Response Failed: 0
Send TPS: 4762 Max RT: 244 Average RT:   0.210 Send Failed: 0 Response Failed: 0
Send TPS: 4663 Max RT: 244 Average RT:   0.214 Send Failed: 0 Response Failed: 0
Send TPS: 4648 Max RT: 244 Average RT:   0.215 Send Failed: 0 Response Failed: 0
Send TPS: 4778 Max RT: 244 Average RT:   0.209 Send Failed: 0 Response Failed: 0
Send TPS: 4737 Max RT: 244 Average RT:   0.211 Send Failed: 0 Response Failed: 0
Send TPS: 4523 Max RT: 244 Average RT:   0.221 Send Failed: 0 Response Failed: 0
Send TPS: 4544 Max RT: 244 Average RT:   0.220 Send Failed: 0 Response Failed: 0
Send TPS: 4683 Max RT: 244 Average RT:   0.213 Send Failed: 0 Response Failed: 0
Send TPS: 4838 Max RT: 244 Average RT:   0.207 Send Failed: 0 Response Failed: 0

</code></pre>
<h4><strong>测试场景五</strong></h4>
<p>10 个线程、消息大小为 1K、主题为 8 个队列。以下结果中发送最大 TPS 为 41946，最大 RT 为 259，平均 RT 为 0.24。</p>
<pre><code>sh producer.sh -t cluster-perf-tst8 -w 10 -s 1024 -n x.x.x.x:9876
Send TPS: 40274 Max RT: 259 Average RT:   0.248 Send Failed: 0 Response Failed: 0
Send TPS: 41421 Max RT: 259 Average RT:   0.241 Send Failed: 0 Response Failed: 0
Send TPS: 43185 Max RT: 259 Average RT:   0.231 Send Failed: 0 Response Failed: 0
Send TPS: 40654 Max RT: 259 Average RT:   0.246 Send Failed: 0 Response Failed: 0
Send TPS: 40744 Max RT: 259 Average RT:   0.245 Send Failed: 0 Response Failed: 0
Send TPS: 41946 Max RT: 259 Average RT:   0.238 Send Failed: 0 Response Failed: 0

</code></pre>
<h4><strong>测试场景六</strong></h4>
<p>10 个线程、消息大小为 3K、主题为 8 个队列。以下结果中发送最大 TPS 为 40927，最大 RT 为 265，平均 RT 为 0.25。</p>
<pre><code>sh producer.sh -t cluster-perf-tst8 -w 10 -s 3072 -n x.x.x.x:9876
Send TPS: 40085 Max RT: 265 Average RT:   0.249 Send Failed: 0 Response Failed: 0
Send TPS: 37710 Max RT: 265 Average RT:   0.265 Send Failed: 0 Response Failed: 0
Send TPS: 39305 Max RT: 265 Average RT:   0.254 Send Failed: 0 Response Failed: 0
Send TPS: 39881 Max RT: 265 Average RT:   0.251 Send Failed: 0 Response Failed: 0
Send TPS: 38428 Max RT: 265 Average RT:   0.260 Send Failed: 0 Response Failed: 0
Send TPS: 39280 Max RT: 265 Average RT:   0.255 Send Failed: 0 Response Failed: 0
Send TPS: 38539 Max RT: 265 Average RT:   0.259 Send Failed: 0 Response Failed: 0
Send TPS: 40927 Max RT: 265 Average RT:   0.244 Send Failed: 0 Response Failed: 0

</code></pre>
<h4><strong>测试场景七</strong></h4>
<p>10 个线程、消息大小为 1K、主题为 16 个队列。以下结果中发送最大 TPS 为 42365，最大 RT 为 243，平均 RT 为 0.23。</p>
<pre><code>sh producer.sh -t cluster-perf-tst16 -w 10 -s 1024 -n x.x.x.x:9876
Send TPS: 41301 Max RT: 243 Average RT:   0.242 Send Failed: 0 Response Failed: 0
Send TPS: 42365 Max RT: 243 Average RT:   0.236 Send Failed: 0 Response Failed: 0
Send TPS: 42181 Max RT: 243 Average RT:   0.237 Send Failed: 0 Response Failed: 0
Send TPS: 42261 Max RT: 243 Average RT:   0.237 Send Failed: 0 Response Failed: 0
Send TPS: 40831 Max RT: 243 Average RT:   0.245 Send Failed: 0 Response Failed: 0
Send TPS: 43010 Max RT: 243 Average RT:   0.232 Send Failed: 0 Response Failed: 0
Send TPS: 41871 Max RT: 243 Average RT:   0.239 Send Failed: 0 Response Failed: 0
Send TPS: 40970 Max RT: 243 Average RT:   0.244 Send Failed: 0 Response Failed: 0

</code></pre>
<h4><strong>测试场景八</strong></h4>
<p>10 个线程、消息大小为 3K、主题为 16 个队列。以下结果中发送最大 TPS 为 39976，最大 RT 为 237，平均 RT 为 0.25。</p>
<pre><code>sh producer.sh -t cluster-perf-tst16 -w 10 -s 3072 -n x.x.x.x:9876
Send TPS: 36245 Max RT: 237 Average RT:   0.276 Send Failed: 0 Response Failed: 0
Send TPS: 38713 Max RT: 237 Average RT:   0.258 Send Failed: 0 Response Failed: 0
Send TPS: 36327 Max RT: 237 Average RT:   0.275 Send Failed: 0 Response Failed: 0
Send TPS: 39005 Max RT: 237 Average RT:   0.256 Send Failed: 0 Response Failed: 0
Send TPS: 37926 Max RT: 237 Average RT:   0.264 Send Failed: 0 Response Failed: 0
Send TPS: 38804 Max RT: 237 Average RT:   0.258 Send Failed: 0 Response Failed: 0
Send TPS: 39976 Max RT: 237 Average RT:   0.250 Send Failed: 0 Response Failed: 0

</code></pre>
<h4><strong>测试场景九</strong></h4>
<p>30 个线程、消息大小为 1K、主题为 8 个队列。以下结果中发送最大 TPS 为 89288，最大 RT 为 309，平均 RT 为 0.34。</p>
<pre><code>sh producer.sh -t cluster-perf-tst8 -w 30 -s 1024 -n x.x.x.x:9876
Send TPS: 86259 Max RT: 309 Average RT:   0.348 Send Failed: 0 Response Failed: 0
Send TPS: 85335 Max RT: 309 Average RT:   0.351 Send Failed: 0 Response Failed: 0
Send TPS: 81850 Max RT: 309 Average RT:   0.366 Send Failed: 0 Response Failed: 0
Send TPS: 87712 Max RT: 309 Average RT:   0.342 Send Failed: 0 Response Failed: 0
Send TPS: 89288 Max RT: 309 Average RT:   0.336 Send Failed: 0 Response Failed: 0
Send TPS: 86732 Max RT: 309 Average RT:   0.346 Send Failed: 0 Response Failed: 0

</code></pre>
<h4><strong>测试场景十</strong></h4>
<p>30 个线程、消息大小为 3K、主题为 8 个队列。以下结果中发送最大 TPS 为 77792，最大 RT 为 334，平均 RT 为 0.42。</p>
<pre><code>sh producer.sh -t cluster-perf-tst8 -w 30 -s 3072 -n x.x.x.x:9876
Send TPS: 74085 Max RT: 334 Average RT:   0.405 Send Failed: 0 Response Failed: 0
Send TPS: 71014 Max RT: 334 Average RT:   0.422 Send Failed: 0 Response Failed: 0
Send TPS: 77792 Max RT: 334 Average RT:   0.386 Send Failed: 0 Response Failed: 0
Send TPS: 73913 Max RT: 334 Average RT:   0.406 Send Failed: 0 Response Failed: 0
Send TPS: 77337 Max RT: 334 Average RT:   0.392 Send Failed: 0 Response Failed: 0
Send TPS: 72184 Max RT: 334 Average RT:   0.416 Send Failed: 0 Response Failed: 0
Send TPS: 77271 Max RT: 334 Average RT:   0.388 Send Failed: 0 Response Failed: 0
Send TPS: 75016 Max RT: 334 Average RT:   0.400 Send Failed: 0 Response Failed: 0

</code></pre>
<h4><strong>测试场景十一</strong></h4>
<p>30 个线程、消息大小为 1K、主题为 16 个队列。以下结果中发送最大 TPS 为 87009，最大 RT 为 306，平均 RT 为 0.34。</p>
<pre><code>sh producer.sh -t zms-clusterB-perf-tst16 -w 30 -s 1024 -n x.x.x.x:9876
Send TPS: 82946 Max RT: 306 Average RT:   0.362 Send Failed: 0 Response Failed: 0
Send TPS: 86902 Max RT: 306 Average RT:   0.345 Send Failed: 0 Response Failed: 0
Send TPS: 83157 Max RT: 306 Average RT:   0.365 Send Failed: 0 Response Failed: 0
Send TPS: 86804 Max RT: 306 Average RT:   0.345 Send Failed: 0 Response Failed: 0
Send TPS: 87009 Max RT: 306 Average RT:   0.345 Send Failed: 0 Response Failed: 0
Send TPS: 80219 Max RT: 306 Average RT:   0.374 Send Failed: 0 Response Failed: 0

</code></pre>
<h4><strong>测试场景十二</strong></h4>
<p>30 个线程、消息大小为 3K、主题为 16 个队列。以下结果中发送最大 TPS 为 78555，最大 RT 为 329，平均 RT 为 0.40。</p>
<pre><code>sh producer.sh -t cluster-perf-tst16 -w 30 -s 3072 -n x.x.x.x:9876
Send TPS: 73864 Max RT: 329 Average RT:   0.403 Send Failed: 0 Response Failed: 0
Send TPS: 78555 Max RT: 329 Average RT:   0.382 Send Failed: 0 Response Failed: 0
Send TPS: 75200 Max RT: 329 Average RT:   0.406 Send Failed: 0 Response Failed: 0
Send TPS: 73925 Max RT: 329 Average RT:   0.406 Send Failed: 0 Response Failed: 0
Send TPS: 69955 Max RT: 329 Average RT:   0.429 Send Failed: 0 Response Failed: 0

</code></pre>
<h4><strong>测试场景十三</strong></h4>
<p>45 个线程、消息大小为 1K、主题为 8 个队列。以下结果中发送最大 TPS 为 96340，最大 RT 为 2063，平均 RT 为 0.48。</p>
<pre><code>sh producer.sh -t cluster-perf-tst8 -w 45 -s 1024 -n x.x.x.x:9876
Send TPS: 91266 Max RT: 2063 Average RT:   0.493 Send Failed: 0 Response Failed: 0
Send TPS: 87279 Max RT: 2063 Average RT:   0.515 Send Failed: 0 Response Failed: 0
Send TPS: 92130 Max RT: 2063 Average RT:   0.487 Send Failed: 0 Response Failed: 1
Send TPS: 95227 Max RT: 2063 Average RT:   0.472 Send Failed: 0 Response Failed: 1
Send TPS: 96340 Max RT: 2063 Average RT:   0.467 Send Failed: 0 Response Failed: 1
Send TPS: 84272 Max RT: 2063 Average RT:   0.534 Send Failed: 0 Response Failed: 1

</code></pre>
<h4><strong>测试场景十四</strong></h4>
<p>45 个线程、消息大小为 3K、主题为 8 个队列。以下结果中发送最大 TPS 为 90403，最大 RT 为 462，平均 RT 为 0.52。</p>
<pre><code>sh producer.sh -t cluster-perf-tst8 -w 45 -s 3072 -n 192.168.x.x:9876
Send TPS: 89334 Max RT: 462 Average RT:   0.503 Send Failed: 0 Response Failed: 0
Send TPS: 84237 Max RT: 462 Average RT:   0.534 Send Failed: 0 Response Failed: 0
Send TPS: 86051 Max RT: 462 Average RT:   0.523 Send Failed: 0 Response Failed: 0
Send TPS: 86475 Max RT: 462 Average RT:   0.520 Send Failed: 0 Response Failed: 0
Send TPS: 86088 Max RT: 462 Average RT:   0.523 Send Failed: 0 Response Failed: 0
Send TPS: 90403 Max RT: 462 Average RT:   0.498 Send Failed: 0 Response Failed: 0
Send TPS: 84229 Max RT: 462 Average RT:   0.534 Send Failed: 0 Response Failed: 0

</code></pre>
<h4><strong>测试场景十五</strong></h4>
<p>45 个线程、消息大小为 1K、主题为 16 个队列。以下结果中发送最大 TPS 为 100158，最大 RT 为 604，平均 RT 为 0.49。</p>
<pre><code>sh producer.sh -t cluster-perf-tst16 -w 45 -s 1024 -n x.x.x.:9876
Send TPS: 91724 Max RT: 604 Average RT:   0.490 Send Failed: 0 Response Failed: 0
Send TPS: 90414 Max RT: 604 Average RT:   0.498 Send Failed: 0 Response Failed: 0
Send TPS: 89904 Max RT: 604 Average RT:   0.500 Send Failed: 0 Response Failed: 0
Send TPS: 100158 Max RT: 604 Average RT:   0.449 Send Failed: 0 Response Failed: 0
Send TPS: 99658 Max RT: 604 Average RT:   0.451 Send Failed: 0 Response Failed: 0
Send TPS: 92440 Max RT: 604 Average RT:   0.489 Send Failed: 0 Response Failed: 0

</code></pre>
<h4><strong>测试场景十六</strong></h4>
<p>45 个线程、消息大小为 3K、主题为 16 个队列。以下结果中发送最大 TPS 为 77297，最大 RT 为 436，平均 RT 为 0.39。</p>
<pre><code>sh producer.sh -t cluster-perf-tst16 -w 30 -s 3072 -n x.x.x.x:9876
Send TPS: 75159 Max RT: 436 Average RT:   0.399 Send Failed: 0 Response Failed: 0
Send TPS: 75315 Max RT: 436 Average RT:   0.398 Send Failed: 0 Response Failed: 0
Send TPS: 77297 Max RT: 436 Average RT:   0.388 Send Failed: 0 Response Failed: 0
Send TPS: 72188 Max RT: 436 Average RT:   0.415 Send Failed: 0 Response Failed: 0
Send TPS: 77525 Max RT: 436 Average RT:   0.387 Send Failed: 0 Response Failed: 0
Send TPS: 71535 Max RT: 436 Average RT:   0.422 Send Failed: 0 Response Failed: 0

</code></pre>
<h4><strong>测试场景十七</strong></h4>
<p>60 个线程、消息大小为 1K、主题为 8 个队列。以下结果中发送最大 TPS 为 111395，最大 RT 为 369，平均 RT 为 0.53。</p>
<pre><code>sh producer.sh -t cluster-perf-tst8 -w 60 -s 1024 -n x.x.x.x:9876
Send TPS: 110067 Max RT: 369 Average RT:   0.545 Send Failed: 0 Response Failed: 0
Send TPS: 111395 Max RT: 369 Average RT:   0.538 Send Failed: 0 Response Failed: 0
Send TPS: 103114 Max RT: 369 Average RT:   0.582 Send Failed: 0 Response Failed: 0
Send TPS: 107466 Max RT: 369 Average RT:   0.558 Send Failed: 0 Response Failed: 0
Send TPS: 106655 Max RT: 369 Average RT:   0.562 Send Failed: 0 Response Failed: 0
Send TPS: 107241 Max RT: 369 Average RT:   0.559 Send Failed: 0 Response Failed: 1
Send TPS: 110672 Max RT: 369 Average RT:   0.540 Send Failed: 0 Response Failed: 1
Send TPS: 109037 Max RT: 369 Average RT:   0.552 Send Failed: 0 Response Failed: 1

</code></pre>
<h4><strong>测试场景十八</strong></h4>
<p>60 个线程、消息大小为 3K、主题为 8 个队列。以下结果中发送最大 TPS 为 99535，最大 RT 为 583，平均 RT 为 0.64。</p>
<pre><code>sh producer.sh -t cluster-perf-tst8 -w 60 -s 3072 -n 192.168.x.x:9876
Send TPS: 92572 Max RT: 583 Average RT:   0.648 Send Failed: 0 Response Failed: 0
Send TPS: 95163 Max RT: 583 Average RT:   0.640 Send Failed: 0 Response Failed: 1
Send TPS: 93823 Max RT: 583 Average RT:   0.654 Send Failed: 0 Response Failed: 1
Send TPS: 97091 Max RT: 583 Average RT:   0.628 Send Failed: 0 Response Failed: 1
Send TPS: 98205 Max RT: 583 Average RT:   0.628 Send Failed: 0 Response Failed: 1
Send TPS: 99535 Max RT: 583 Average RT:   0.596 Send Failed: 0 Response Failed: 3

</code></pre>
<h4><strong>测试场景十九</strong></h4>
<p>60 个线程、消息大小为 1K、主题为 16 个队列。以下结果中发送最大 TPS 为 111667，最大 RT 为 358，平均 RT 为 0.55。</p>
<pre><code>sh producer.sh -t cluster-perf-tst16 -w 60 -s 1024 -n x.x.x.x:9876
Send TPS: 105229 Max RT: 358 Average RT:   0.578 Send Failed: 0 Response Failed: 0
Send TPS: 103003 Max RT: 358 Average RT:   0.582 Send Failed: 0 Response Failed: 0
Send TPS: 95497 Max RT: 358 Average RT:   0.628 Send Failed: 0 Response Failed: 0
Send TPS: 108878 Max RT: 358 Average RT:   0.551 Send Failed: 0 Response Failed: 0
Send TPS: 109265 Max RT: 358 Average RT:   0.549 Send Failed: 0 Response Failed: 0
Send TPS: 105545 Max RT: 358 Average RT:   0.568 Send Failed: 0 Response Failed: 0
Send TPS: 111667 Max RT: 358 Average RT:   0.537 Send Failed: 0 Response Failed: 0

</code></pre>
<h4><strong>测试场景二十</strong></h4>
<p>60 个线程、消息大小为 3K、主题为 16 个队列。以下结果中发送最大 TPS 为 101073，最大 RT 为 358，平均 RT 为 0.61。</p>
<pre><code>sh producer.sh -t cluster-perf-tst16 -w 60 -s 3072 -n x.x.x.x:9876
Send TPS: 98899 Max RT: 358 Average RT:   0.606 Send Failed: 0 Response Failed: 0
Send TPS: 101073 Max RT: 358 Average RT:   0.594 Send Failed: 0 Response Failed: 0
Send TPS: 97295 Max RT: 358 Average RT:   0.617 Send Failed: 0 Response Failed: 0
Send TPS: 97923 Max RT: 358 Average RT:   0.609 Send Failed: 0 Response Failed: 1
Send TPS: 96111 Max RT: 358 Average RT:   0.620 Send Failed: 0 Response Failed: 2
Send TPS: 93873 Max RT: 358 Average RT:   0.639 Send Failed: 0 Response Failed: 2
Send TPS: 96466 Max RT: 358 Average RT:   0.622 Send Failed: 0 Response Failed: 2
Send TPS: 96579 Max RT: 358 Average RT:   0.621 Send Failed: 0 Response Failed: 2

</code></pre>
<h4><strong>测试场景二十一</strong></h4>
<p>75 个线程、消息大小为 1K、主题为 8 个队列。以下结果中发送最大 TPS 为 112707，最大 RT 为 384，平均 RT 为 0.68。</p>
<pre><code>sh producer.sh -t cluster-perf-tst8 -w 75 -s 1024 -n x.x.x.x:9876
Send TPS: 108367 Max RT: 384 Average RT:   0.692 Send Failed: 0 Response Failed: 0
Send TPS: 107516 Max RT: 384 Average RT:   0.701 Send Failed: 0 Response Failed: 0
Send TPS: 110974 Max RT: 384 Average RT:   0.680 Send Failed: 0 Response Failed: 0
Send TPS: 109754 Max RT: 384 Average RT:   0.683 Send Failed: 0 Response Failed: 0
Send TPS: 111917 Max RT: 384 Average RT:   0.670 Send Failed: 0 Response Failed: 0
Send TPS: 104764 Max RT: 384 Average RT:   0.712 Send Failed: 0 Response Failed: 1
Send TPS: 112208 Max RT: 384 Average RT:   0.668 Send Failed: 0 Response Failed: 1
Send TPS: 112707 Max RT: 384 Average RT:   0.665 Send Failed: 0 Response Failed: 1

</code></pre>
<h4><strong>测试场景二十二</strong></h4>
<p>75 个线程、消息大小为 3K、主题为 8 个队列。以下结果中发送最大 TPS 为 103953，最大 RT 为 370，平均 RT 为 0.74。</p>
<pre><code>sh producer.sh -t cluster-perf-tst8 -w 75 -s 3072 -n x.x.x.x:9876
Send TPS: 102311 Max RT: 370 Average RT:   0.733 Send Failed: 0 Response Failed: 0
Send TPS: 93722 Max RT: 370 Average RT:   0.800 Send Failed: 0 Response Failed: 0
Send TPS: 101091 Max RT: 370 Average RT:   0.742 Send Failed: 0 Response Failed: 0
Send TPS: 100404 Max RT: 370 Average RT:   0.747 Send Failed: 0 Response Failed: 0
Send TPS: 102328 Max RT: 370 Average RT:   0.733 Send Failed: 0 Response Failed: 0
Send TPS: 103953 Max RT: 370 Average RT:   0.722 Send Failed: 0 Response Failed: 0
Send TPS: 103454 Max RT: 370 Average RT:   0.725 Send Failed: 0 Response Failed: 0

</code></pre>
<h4><strong>测试场景二十三</strong></h4>
<p>75 个线程、消息大小为 1K、主题为 16 个队列。以下结果中发送最大 TPS 为 115659，最大 RT 为 605，平均 RT 为 0.68。</p>
<pre><code>sh producer.sh -t cluster-perf-tst16 -w 75 -s 1024 -n x.x.x.x:9876
Send TPS: 106813 Max RT: 605 Average RT:   0.687 Send Failed: 0 Response Failed: 0
Send TPS: 110828 Max RT: 605 Average RT:   0.673 Send Failed: 0 Response Failed: 1
Send TPS: 109855 Max RT: 605 Average RT:   0.676 Send Failed: 0 Response Failed: 3
Send TPS: 102741 Max RT: 605 Average RT:   0.730 Send Failed: 0 Response Failed: 3
Send TPS: 110123 Max RT: 605 Average RT:   0.681 Send Failed: 0 Response Failed: 3
Send TPS: 115659 Max RT: 605 Average RT:   0.648 Send Failed: 0 Response Failed: 3
Send TPS: 108157 Max RT: 605 Average RT:   0.693 Send Failed: 0 Response Failed: 3

</code></pre>
<h4><strong>测试场景二十四</strong></h4>
<p>75 个线程、消息大小为 3K、主题为 16 个队列。以下结果中发送最大 TPS 为 99871，最大 RT 为 499，平均 RT 为 0.78。</p>
<pre><code>sh producer.sh -t cluster-perf-tst16 -w 75 -s 3072 -n x.x.x.x:9876
Send TPS: 90459 Max RT: 499 Average RT:   0.829 Send Failed: 0 Response Failed: 0
Send TPS: 96838 Max RT: 499 Average RT:   0.770 Send Failed: 0 Response Failed: 1
Send TPS: 96590 Max RT: 499 Average RT:   0.776 Send Failed: 0 Response Failed: 1
Send TPS: 95137 Max RT: 499 Average RT:   0.788 Send Failed: 0 Response Failed: 1
Send TPS: 89502 Max RT: 499 Average RT:   0.834 Send Failed: 0 Response Failed: 2
Send TPS: 90255 Max RT: 499 Average RT:   0.831 Send Failed: 0 Response Failed: 2
Send TPS: 99871 Max RT: 499 Average RT:   0.725 Send Failed: 0 Response Failed: 9

</code></pre>
<h4><strong>测试场景二十五</strong></h4>
<p>100 个线程、消息大小为 1K、主题为 8 个队列。以下结果中发送最大 TPS 为 126590，最大 RT 为 402，平均 RT 为 0.86。</p>
<pre><code>sh producer.sh -t cluster-perf-tst8 -w 100 -s 1024 -n x.x.x.x:9876
Send TPS: 113204 Max RT: 402 Average RT:   0.883 Send Failed: 0 Response Failed: 0
Send TPS: 114872 Max RT: 402 Average RT:   0.868 Send Failed: 0 Response Failed: 1
Send TPS: 116261 Max RT: 402 Average RT:   0.860 Send Failed: 0 Response Failed: 1
Send TPS: 118116 Max RT: 402 Average RT:   0.847 Send Failed: 0 Response Failed: 1
Send TPS: 112594 Max RT: 402 Average RT:   0.888 Send Failed: 0 Response Failed: 1
Send TPS: 124407 Max RT: 402 Average RT:   0.801 Send Failed: 0 Response Failed: 2
Send TPS: 126590 Max RT: 402 Average RT:   0.790 Send Failed: 0 Response Failed: 2

</code></pre>
<h4><strong>测试场景二十六</strong></h4>
<p>100 个线程、消息大小为 3K、主题为 8 个队列。以下结果中发送最大 TPS 为 108616，最大 RT 为 426，平均 RT 为 0.93。</p>
<pre><code>sh producer.sh -t cluster-perf-tst8 -w 100 -s 3072 -n x.x.x.x:9876
Send TPS: 106723 Max RT: 426 Average RT:   0.937 Send Failed: 0 Response Failed: 0
Send TPS: 104768 Max RT: 426 Average RT:   0.943 Send Failed: 0 Response Failed: 1
Send TPS: 106697 Max RT: 426 Average RT:   0.935 Send Failed: 0 Response Failed: 2
Send TPS: 105147 Max RT: 426 Average RT:   0.951 Send Failed: 0 Response Failed: 2
Send TPS: 105814 Max RT: 426 Average RT:   0.935 Send Failed: 0 Response Failed: 5
Send TPS: 108616 Max RT: 426 Average RT:   0.916 Send Failed: 0 Response Failed: 6
Send TPS: 101429 Max RT: 426 Average RT:   0.986 Send Failed: 0 Response Failed: 6

</code></pre>
<h4><strong>测试场景二十七</strong></h4>
<p>100 个线程、消息大小为 1K、主题为 16 个队列。以下结果中发送最大 TPS 为 123424，最大 RT 为 438，平均 RT 为 0.86。</p>
<pre><code>sh producer.sh -t cluster-perf-tst16 -w 100 -s 1024 -n x.x.x.x:9876
Send TPS: 123424 Max RT: 438 Average RT:   0.805 Send Failed: 0 Response Failed: 0
Send TPS: 111418 Max RT: 438 Average RT:   0.897 Send Failed: 0 Response Failed: 0
Send TPS: 110360 Max RT: 438 Average RT:   0.905 Send Failed: 0 Response Failed: 0
Send TPS: 118734 Max RT: 438 Average RT:   0.842 Send Failed: 0 Response Failed: 0
Send TPS: 120725 Max RT: 438 Average RT:   0.816 Send Failed: 0 Response Failed: 4
Send TPS: 113823 Max RT: 438 Average RT:   0.878 Send Failed: 0 Response Failed: 4
Send TPS: 115639 Max RT: 438 Average RT:   0.865 Send Failed: 0 Response Failed: 4
Send TPS: 112787 Max RT: 438 Average RT:   0.889 Send Failed: 0 Response Failed: 4
Send TPS: 106677 Max RT: 438 Average RT:   0.937 Send Failed: 0 Response Failed: 4
Send TPS: 112635 Max RT: 438 Average RT:   0.888 Send Failed: 0 Response Failed: 4
Send TPS: 108470 Max RT: 438 Average RT:   0.922 Send Failed: 0 Response Failed: 4

</code></pre>
<h4><strong>测试场景二十八</strong></h4>
<p>100 个线程、消息大小为 3K、主题为 16 个队列。以下结果中发送最大 TPS 为 103664，最大 RT 为 441，平均 RT 为 0.96。</p>
<pre><code>sh producer.sh -t cluster-perf-tst16 -w 100 -s 3072 -n x.x.x.x:9876
Send TPS: 93374 Max RT: 441 Average RT:   1.071 Send Failed: 0 Response Failed: 3
Send TPS: 98421 Max RT: 441 Average RT:   1.017 Send Failed: 0 Response Failed: 3
Send TPS: 103664 Max RT: 441 Average RT:   0.964 Send Failed: 0 Response Failed: 4
Send TPS: 98234 Max RT: 441 Average RT:   0.995 Send Failed: 0 Response Failed: 6
Send TPS: 103563 Max RT: 441 Average RT:   0.960 Send Failed: 0 Response Failed: 7
Send TPS: 103807 Max RT: 441 Average RT:   0.962 Send Failed: 0 Response Failed: 7
Send TPS: 102715 Max RT: 441 Average RT:   0.973 Send Failed: 0 Response Failed: 7

</code></pre>
<h4><strong>测试场景二十九</strong></h4>
<p>150 个线程、消息大小为 1K、主题为 8 个队列。以下结果中发送最大 TPS 为 124567，最大 RT 为 633，平均 RT 为 1.20。</p>
<pre><code>sh producer.sh -t cluster-perf-tst8 -w 150 -s 1024 -n x.x.x.x:9876
Send TPS: 124458 Max RT: 633 Average RT:   1.205 Send Failed: 0 Response Failed: 0
Send TPS: 124567 Max RT: 633 Average RT:   1.204 Send Failed: 0 Response Failed: 0
Send TPS: 121324 Max RT: 633 Average RT:   1.236 Send Failed: 0 Response Failed: 0
Send TPS: 124928 Max RT: 633 Average RT:   1.201 Send Failed: 0 Response Failed: 0
Send TPS: 122830 Max RT: 633 Average RT:   1.242 Send Failed: 0 Response Failed: 0
Send TPS: 118825 Max RT: 633 Average RT:   1.262 Send Failed: 0 Response Failed: 0
Send TPS: 124085 Max RT: 633 Average RT:   1.209 Send Failed: 0 Response Failed: 0

</code></pre>
<h4><strong>测试场景三十</strong></h4>
<p>150 个线程、消息大小为 3K、主题为 8 个队列。以下结果中发送最大 TPS 为 107032，最大 RT 为 582，平均 RT 为 1.40。</p>
<pre><code>sh producer.sh -t cluster-perf-tst8 -w 150 -s 3072 -n x.x.x.x:9876
Send TPS: 106575 Max RT: 582 Average RT:   1.404 Send Failed: 0 Response Failed: 1
Send TPS: 101830 Max RT: 582 Average RT:   1.477 Send Failed: 0 Response Failed: 1
Send TPS: 99666 Max RT: 582 Average RT:   1.505 Send Failed: 0 Response Failed: 1
Send TPS: 102139 Max RT: 582 Average RT:   1.465 Send Failed: 0 Response Failed: 2
Send TPS: 105405 Max RT: 582 Average RT:   1.419 Send Failed: 0 Response Failed: 3
Send TPS: 107032 Max RT: 582 Average RT:   1.399 Send Failed: 0 Response Failed: 4
Send TPS: 103416 Max RT: 582 Average RT:   1.448 Send Failed: 0 Response Failed: 5

</code></pre>
<h4><strong>测试场景三十一</strong></h4>
<p>150 个线程、消息大小为 1K、主题为 16 个队列。以下结果中发送最大 TPS 为 124474，最大 RT 为 574，平均 RT 为 1.40。</p>
<pre><code>sh producer.sh -t cluster-perf-tst16 -w 150 -s 1024 -n x.x.x.x:9876
Send TPS: 115151 Max RT: 574 Average RT:   1.299 Send Failed: 0 Response Failed: 1
Send TPS: 106960 Max RT: 574 Average RT:   1.402 Send Failed: 0 Response Failed: 1
Send TPS: 116382 Max RT: 574 Average RT:   1.289 Send Failed: 0 Response Failed: 1
Send TPS: 110587 Max RT: 574 Average RT:   1.349 Send Failed: 0 Response Failed: 4
Send TPS: 122832 Max RT: 574 Average RT:   1.220 Send Failed: 0 Response Failed: 4
Send TPS: 124474 Max RT: 574 Average RT:   1.213 Send Failed: 0 Response Failed: 4
Send TPS: 112153 Max RT: 574 Average RT:   1.337 Send Failed: 0 Response Failed: 4
Send TPS: 120450 Max RT: 574 Average RT:   1.261 Send Failed: 0 Response Failed: 4

</code></pre>
<h4><strong>测试场景三十二</strong></h4>
<p>150 个线程、消息大小为 3K、主题为 16 个队列。以下结果中发送最大 TPS 为 111285，最大 RT 为 535，平均 RT 为 1.42。</p>
<pre><code>sh producer.sh -t cluster-perf-tst16 -w 150 -s 3072 -n x.x.x.x:9876
Send TPS: 105061 Max RT: 535 Average RT:   1.428 Send Failed: 0 Response Failed: 0
Send TPS: 102117 Max RT: 535 Average RT:   1.465 Send Failed: 0 Response Failed: 1
Send TPS: 105569 Max RT: 535 Average RT:   1.421 Send Failed: 0 Response Failed: 1
Send TPS: 100689 Max RT: 535 Average RT:   1.489 Send Failed: 0 Response Failed: 2
Send TPS: 108464 Max RT: 535 Average RT:   1.381 Send Failed: 0 Response Failed: 2
Send TPS: 111285 Max RT: 535 Average RT:   1.348 Send Failed: 0 Response Failed: 2
Send TPS: 103406 Max RT: 535 Average RT:   1.451 Send Failed: 0 Response Failed: 2
Send TPS: 109203 Max RT: 535 Average RT:   1.388 Send Failed: 0 Response Failed: 2

</code></pre>
<h4><strong>测试场景三十三</strong></h4>
<p>200 个线程、消息大小为 1K、主题为 8 个队列。以下结果中发送最大 TPS 为 126170，最大 RT 为 628，平均 RT 为 1.71。</p>
<pre><code>sh producer.sh -t cluster-perf-tst8 -w 200 -s 1024 -n x.x.x.x:9876
Send TPS: 117965 Max RT: 628 Average RT:   1.674 Send Failed: 0 Response Failed: 7
Send TPS: 115583 Max RT: 628 Average RT:   1.715 Send Failed: 0 Response Failed: 12
Send TPS: 118732 Max RT: 628 Average RT:   1.672 Send Failed: 0 Response Failed: 16
Send TPS: 126170 Max RT: 628 Average RT:   1.582 Send Failed: 0 Response Failed: 17
Send TPS: 116203 Max RT: 628 Average RT:   1.719 Send Failed: 0 Response Failed: 18
Send TPS: 114793 Max RT: 628 Average RT:   1.739 Send Failed: 0 Response Failed: 19

</code></pre>
<h4><strong>测试场景三十四</strong></h4>
<p>200 个线程、消息大小为 3K、主题为 8 个队列。以下结果中发送最大 TPS 为 110892，最大 RT 为 761，平均 RT 为 1.80。</p>
<pre><code>sh producer.sh -t cluster-perf-tst8 -w 200 -s 3072 -n x.x.x.x:9876
Send TPS: 107240 Max RT: 761 Average RT:   1.865 Send Failed: 0 Response Failed: 0
Send TPS: 104585 Max RT: 761 Average RT:   1.906 Send Failed: 0 Response Failed: 2
Send TPS: 110892 Max RT: 761 Average RT:   1.803 Send Failed: 0 Response Failed: 2
Send TPS: 105414 Max RT: 761 Average RT:   1.898 Send Failed: 0 Response Failed: 2
Send TPS: 105904 Max RT: 761 Average RT:   1.885 Send Failed: 0 Response Failed: 3
Send TPS: 110748 Max RT: 761 Average RT:   1.806 Send Failed: 0 Response Failed: 3

</code></pre>
<h4><strong>测试场景三十五</strong></h4>
<p>200 个线程、消息大小为 1K、主题为 16 个队列。以下结果中发送最大 TPS 为 124760，最大 RT 为 601，平均 RT 为 1.63。</p>
<pre><code>sh producer.sh -t cluster-perf-tst16 -w 200 -s 1024 -n x.x.x.x:9876
Send TPS: 118892 Max RT: 601 Average RT:   1.679 Send Failed: 0 Response Failed: 4
Send TPS: 118839 Max RT: 601 Average RT:   1.668 Send Failed: 0 Response Failed: 12
Send TPS: 117122 Max RT: 601 Average RT:   1.704 Send Failed: 0 Response Failed: 12
Send TPS: 122670 Max RT: 601 Average RT:   1.630 Send Failed: 0 Response Failed: 12
Send TPS: 119592 Max RT: 601 Average RT:   1.672 Send Failed: 0 Response Failed: 12
Send TPS: 121243 Max RT: 601 Average RT:   1.649 Send Failed: 0 Response Failed: 12
Send TPS: 124760 Max RT: 601 Average RT:   1.603 Send Failed: 0 Response Failed: 12
Send TPS: 124354 Max RT: 601 Average RT:   1.608 Send Failed: 0 Response Failed: 12
Send TPS: 119272 Max RT: 601 Average RT:   1.677 Send Failed: 0 Response Failed: 12

</code></pre>
<h4><strong>测试场景三十六</strong></h4>
<p>200 个线程、消息大小为 3K、主题为 16 个队列。以下结果中发送最大 TPS 为 111201，最大 RT 为 963，平均 RT 为 1.88。</p>
<pre><code>sh producer.sh -t cluster-perf-tst16 -w 200 -s 3072 -n x.x.x.x:9876
Send TPS: 105091 Max RT: 963 Average RT:   1.896 Send Failed: 0 Response Failed: 4
Send TPS: 106243 Max RT: 963 Average RT:   1.882 Send Failed: 0 Response Failed: 4
Send TPS: 103994 Max RT: 963 Average RT:   1.958 Send Failed: 0 Response Failed: 5
Send TPS: 109741 Max RT: 963 Average RT:   1.822 Send Failed: 0 Response Failed: 5
Send TPS: 103788 Max RT: 963 Average RT:   1.927 Send Failed: 0 Response Failed: 5
Send TPS: 110597 Max RT: 963 Average RT:   1.805 Send Failed: 0 Response Failed: 6
Send TPS: 111201 Max RT: 963 Average RT:   1.798 Send Failed: 0 Response Failed: 6

</code></pre>
<h3>总结</h3>
<p>通过上面的性能压测，可以看出最高 TPS 为 12.6 万。那可以确定集群的理论承载值为 12 万左右，日常流量控制在 4 万左右，当超过 4 万时新申请的主题分配到其他集群。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="15&#32;RocketMQ&#32;常用命令实战.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="17&#32;RocketMQ&#32;集群性能调优.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434b07c9d370ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
