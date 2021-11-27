<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>09 DefaultMQPushConsumer 核心参数与工作原理.md</title>
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

                    <a class="current-tab" href="09&#32;DefaultMQPushConsumer&#32;核心参数与工作原理.md">09 DefaultMQPushConsumer 核心参数与工作原理.md</a>
                    

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
                        <div><h1>09 DefaultMQPushConsumer 核心参数与工作原理</h1>
<p>PUSH 模式是对 PULL 模式的封装，类似于一个高级 API，用户使用起来将非常简单，基本将消息消费所需要解决的问题都封装好了，故使用起来将变得简单。与此同时，需要将其用好，那还是需要了解其内部的工作原理以及 PUSH 模式支持哪些参数，这些参数是如何工作的，在使用时有什么注意的呢？</p>
<h3>DefaultMQPushConsumer 核心参数一览与内部原理</h3>
<p>DefaultMQPushConsumer 的核心参数一览如下。</p>
<p><strong>InternalLogger log</strong></p>
<p>这个是消费者一个 final 的属性，用来记录 RocketMQ Consumer 在运作过程中的一些日志，其日志文件默认路径为 <code>${user.home}/logs/rocketmqlogs/rocketmq_cliente.log</code>。</p>
<p><strong>String consumerGroup</strong></p>
<p>消费组的名称，在 RocketMQ 中，对于消费中来说，一个消费组就是一个独立的隔离单位，例如多个消费组订阅同一个主题，其消息进度（消息处理的进展）是相互独立的，两者不会有任何的干扰。</p>
<p><strong>MessageModel messageModel</strong></p>
<p>消息组消息消费模式，在 RocketMQ 中支持集群模式、广播模式。集群模式值得是一个消费组内多个消费者共同消费一个 Topic 中的消息，即一条消息只会被集群内的某一个消费者处理；而广播模式是指一个消费组内的每一个消费者负责 Topic 中的所有消息。</p>
<p><strong>ConsumeFromWhere consumeFromWhere</strong></p>
<p><strong>一个消费者初次启动时</strong>（即消费进度管理器中无法查询到该消费组的进度）时从哪个位置开始消费的策略，可选值如下所示：</p>
<ul>
<li>CONSUME_FROM_LAST_OFFSET：从最新的消息开始消费。</li>
<li>CONSUME_FROM_FIRST_OFFSET：从最新的位点开始消费。</li>
<li>CONSUME_FROM_TIMESTAMP：从指定的时间戳开始消费，这里的实现思路是从 Broker 服务器寻找消息的存储时间小于或等于指定时间戳中最大的消息偏移量的消息，从这条消息开始消费。</li>
</ul>
<p><strong>String consumeTimestamp</strong></p>
<p>指定从什么时间戳开始消费，其格式为 yyyyMMddHHmmss，默认值为 30 分钟之前，该参数只在 consumeFromWhere 为 CONSUME_FROM_TIMESTAMP 时生效。</p>
<p><strong>AllocateMessageQueueStrategy allocateMessageQueueStrategy</strong></p>
<p>消息队列负载算法。主要解决的问题是消息消费队列在各个消费者之间的负载均衡策略，例如一个 Topic 有８个队列，一个消费组中有３个消费者，那这三个消费者各自去消费哪些队列。</p>
<p>RocketMQ 默认提供了如下负载均衡算法：</p>
<ul>
<li>AllocateMessageQueueAveragely：平均连续分配算法。</li>
<li>AllocateMessageQueueAveragelyByCircle：平均轮流分配算法。</li>
<li>AllocateMachineRoomNearby：机房内优先就近分配。</li>
<li>AllocateMessageQueueByConfig：手动指定，这个通常需要配合配置中心，在消费者启动时，首先先创建 AllocateMessageQueueByConfig 对象，然后根据配置中心的配置，再根据当前的队列信息，进行分配，即该方法不具备队列的自动负载，在 Broker 端进行队列扩容时，无法自动感知，需要手动变更配置。</li>
<li>AllocateMessageQueueByMachineRoom：消费指定机房中的队列，该分配算法首先需要调用该策略的 <code>setConsumeridcs(Set&lt;String&gt; consumerIdCs)</code> 方法，用于设置需要消费的机房，将刷选出来的消息按平均连续分配算法进行队列负载。</li>
</ul>
<p><strong>AllocateMessageQueueConsistentHash</strong></p>
<p>一致性 Hash 算法。</p>
<p><strong>OffsetStore offsetStore</strong></p>
<p>消息进度存储管理器，该属性为私有属性，不能通过 API 进行修改，该参数主要是根据消费模式在内部自动创建，RocketMQ 在广播消息、集群消费两种模式下消息消费进度的存储策略会有所不同。</p>
<ul>
<li>集群模式：RocketMQ 会将消息消费进度存储在 Broker 服务器，存储路径为 <code>${ROCKET_HOME}/store/config/ consumerOffset.json</code> 文件中。</li>
<li>广播模式：RocketMQ 会将消息消费进存在在消费端所在的机器上，存储路径为 <code>${user.home}/.rocketmq_offsets</code> 中。</li>
</ul>
<p>为了方便大家对消息消费进度有一个直接的理解，下面给出我本地测试时 Broker 集群中的消息消费进度文件，其截图如下：</p>
<p><img src="assets/20200814230847619.png" alt="1" /></p>
<p>消息消费进度，首先使用 <a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="c6b2a9b6afa586a5a9a8b5b3aba3b481b4a9b3b6">[email&#160;protected]</a> 为键，其值是一个 Map，键为 Topic 的队列序列，值为当前的消息消费位点。</p>
<pre><code>int consumeThreadMin

</code></pre>
<p>消费者每一个消费组线程池中最小的线程数量，默认为 20。在 RocketMQ 消费者中，会为每一个消费者创建一个独立的线程池。</p>
<pre><code>int consumeThreadMax

</code></pre>
<p>消费者最大线程数量，在当前的 RocketMQ 版本中，该参数通常与 consumeThreadMin 保持一致，大于没有意义，因为 RocketMQ 创建的线程池内部创建的队列为一个无界队列。</p>
<pre><code>int consumeConcurrentlyMaxSpan

</code></pre>
<p>并发消息消费时处理队列中最大偏移量与最小偏移量的差值的阔值，如差值超过该值，触发消费端限流。限流的具体做法是不再向 Broker 拉取该消息队列中的消息，默认值为 2000。</p>
<pre><code>int pullThresholdForQueue

</code></pre>
<p>消费端允许消费端端单队列积压的消息数量，如果处理队列中超过该值，会触发消息消费端的限流。默认值为 1000，不建议修改该值。</p>
<pre><code>pullThresholdSizeForQueue

</code></pre>
<p>消费端允许消费端但队列中挤压的消息体大小，默认为 100MB。</p>
<pre><code>pullThresholdForTopic

</code></pre>
<p>按 Topic 级别进行消息数量限流，默认不开启，为 -1，如果设置该值，会使用该值除以分配给当前消费者的队列数，得到每个消息消费队列的消息阔值，从而改变 pullThresholdForQueue。</p>
<pre><code>pullThresholdSizeForTopic

</code></pre>
<p>按 Topic 级别进行消息消息体大小进行限流，默认不开启，其最终通过改变 pullThresholdSizeForQueue 达到限流效果。</p>
<pre><code>long pullInterval = 0

</code></pre>
<p>消息拉取的间隔，默认 0 表示，消息客户端在拉取一批消息提交到线程池后立即向服务端拉取下一批，PUSH 模式不建议修改该值。</p>
<pre><code>int pullBatchSize = 32

</code></pre>
<p>一次消息拉取请求最多从 Broker 返回的消息条数，默认为 32。</p>
<pre><code>int consumeMessageBatchMaxSize 

</code></pre>
<p>消息消费一次最大消费的消息条数，这个值得是下图中参数 <code>ist&lt;MessageExt&gt; msgs</code> 中消息的最大条数。</p>
<p><img src="assets/20200814230854780.png" alt="2" /></p>
<pre><code>int maxReconsumeTimes 

</code></pre>
<p>消息消费重试次数，并发消费模式下默认重试 16 次后进入到死信队列，如果是顺序消费，重试次数为 Integer.MAX_VALUE。</p>
<pre><code>long suspendCurrentQueueTimeMillis

</code></pre>
<p>消费模式为顺序消费时设置每一次重试的间隔时间，提高重试成功率。</p>
<pre><code>long consumeTimeout = 15

</code></pre>
<p>消息消费超时时间，默认为 15 分钟。</p>
<h3>核心参数工作原理</h3>
<h4><strong>消息消费队列负载算法</strong></h4>
<p>本节将使用图解的方式来阐述 RocketMQ 默认提供的消息消费队列负载机制。</p>
<p><strong>AllocateMessageQueueAveragely</strong></p>
<p>平均连续分配算法。主要的特点是一个消费者分配的消息队列是连续的。</p>
<p><img src="assets/20200814230902879.png" alt="3" /></p>
<p><strong>AllocateMessageQueueAveragelyByCircle</strong></p>
<p>平均轮流分配算法，其分配示例图如下：</p>
<p><img src="assets/20200814230909976.png" alt="4" /></p>
<p><strong>AllocateMachineRoomNearby</strong></p>
<p>机房内优先就近分配。其分配示例图如下：</p>
<p><img src="assets/20200814230918209.png" alt="5" /></p>
<p>上述的背景是一个 MQ 集群的两台 Broker 分别部署在两个不同的机房，每一个机房中都部署了一些消费者，其队列的负载情况是同机房中的消费队列优先被同机房的消费者进行分配，其分配算法可以指定其他的算法，例如示例中的平均分配，但如果机房 B 中的消费者宕机，B 机房中没有存活的消费者，那该机房中的队列会被其他机房中的消费者获取进行消费。</p>
<p><strong>AllocateMessageQueueByConfig</strong></p>
<p>手动指定，这个通常需要配合配置中心，在消费者启动时，首先先创建 AllocateMessageQueueByConfig 对象，然后根据配置中心的配置，再根据当前的队列信息，进行分配，即该方法不具备队列的自动负载，在 Broker 端进行队列扩容时，无法自动感知，需要手动变更配置。</p>
<p><strong>AllocateMessageQueueByMachineRoom</strong></p>
<p>消费指定机房中的队列，该分配算法首先需要调用该策略的 <code>setConsumeridcs(Set&lt;String&gt; consumerIdCs)</code> 方法，用于设置需要消费的机房，将刷选出来的消息按平均连续分配算法进行队列负载，其分配示例图如下所示：</p>
<p><img src="assets/20200814230925817.png" alt="6" /></p>
<p>由于设置 consumerIdCs 为 A 机房，故 B 机房中的队列并不会消息。</p>
<p><strong>AllocateMessageQueueConsistentHash</strong></p>
<p>一致性 Hash 算法，讲真，在消息队列负载这里使用一致性算法，没有任何实际好处，一致性 Hash 算法最佳的使用场景用在 Redis 缓存的分布式领域最适宜。</p>
<h4><strong>PUSH 模型消息拉取机制</strong></h4>
<p>在介绍消息消费端限流机制时，首先用如下简图简单介绍一下 RocketMQ 消息拉取执行模型。</p>
<p><img src="assets/20200814230940226.png" alt="7" /></p>
<p>其核心关键点如下：</p>
<ol>
<li>经过队列负载机制后，会分配给当前消费者一些队列，注意一个消费组可以订阅多个主题，正如上面 pullRequestQueue 中所示，topic_test、topic_test1 这两个主题都分配了一个队列。</li>
<li>轮流从 pullRequestQueue 中取出一个 PullRequest 对象，根据该对象中的拉取偏移量向 Broker 发起拉取请求，默认拉取 32 条，可通过上文中提到的 pullBatchSize 参数进行改变，该方法不仅会返回消息列表，还会返更改 PullRequest 对象中的下一次拉取的偏移量。</li>
<li>接收到 Broker 返回的消息后，会首先放入 ProccessQueue（处理队列），该队列的内部结构为 TreeMap，key 存放的是消息在消息消费队列（consumequeue）中的偏移量，而 value 为具体的消息对象。</li>
<li>然后将拉取到的消息提交到消费组内部的线程池，并立即返回，并将 PullRequest 对象放入到 pullRequestQueue 中，然后取出下一个 PullRequest 对象继续重复消息拉取的流程，从这里可以看出，消息拉取与消息消费是不同的线程。</li>
<li>消息消费组线程池处理完一条消息后，会将消息从 ProccessQueue 中，然后会向 Broker 汇报消息消费进度，以便下次重启时能从上一次消费的位置开始消费。</li>
</ol>
<h4><strong>消息消费进度提交</strong></h4>
<p>通过上面的介绍，想必读者应该对消息消费进度有了一个比较直观的认识，接下来我们再来介绍一下 RocketMQ PUSH 模式的消息消费进度提交机制。</p>
<p>通过上文的消息消费拉取模型可以看出，消息消费组线程池在处理完一条消息后，会将消息从 ProccessQueue 中移除，并向 Broker 汇报消息消费进度，那请大家思考一下下面这个问题：</p>
<p><img src="assets/20200814230947106.png" alt="8" /></p>
<p>例如现在处理队列中有 5 条消息，并且是线程池并发消费，那如果消息偏移量为 3 的消息（3:msg3）先于偏移量为 0、1、2 的消息处理完，那向 Broker 如何汇报消息消费进度呢？</p>
<p>有读者朋友说，消息 msg3 处理完，当然是向 Broker 汇报 msg3 的偏移量作为消息消费进度呀。但细心思考一下，发现如果提交 msg3 的偏移量为消息消费进度，那汇报完毕后如果消费者发生内存溢出等问题导致 JVM 异常退出，msg1 的消息还未处理，然后重启消费者，由于消息消费进度文件中存储的是 msg3 的消息偏移量，会继续从 msg3 开始消费，会造成<strong>消息丢失</strong>。显然这种方式并不可取。</p>
<p>RocketMQ 采取的方式是处理完 msg3 之后，会将 msg3 从消息处理队列中移除，但在向 Broker 汇报消息消费进度时是<strong>取 ProceeQueue 中最小的偏移量为消息消费进度</strong>，即汇报的消息消费进度是 0。</p>
<p><img src="assets/20200814230953825.png" alt="9" /></p>
<p>即如果处理队列如上图所示，那提交的消息进度为 2。但这种方案也并非完美，有可能会造成消息重复消费，例如如果发生内存溢出等异常情况，消费者重新启动，会继续从消息偏移量为 2 的消息开始消费，msg3 就会被消费多次，故<strong>RocketMQ 不保证消息重复消费</strong>。</p>
<p>消息消费进度具体的提交流程如下图所示：</p>
<p><img src="assets/20200815082211329.png" alt="10" /></p>
<p>从这里也可以看成，为了减少消费者与 Broker 的网络交互，提高性能，提交消息消费进度时会首先存入到本地缓存表中，然后定时上报到 Broker，同样 Broker 也会首先存储本地缓存表，然后定时刷写到磁盘。</p>
<h3>小结</h3>
<p>本篇详细介绍了 DefaultMQPushConsumer 的所有可配置参数以及消息消费中消息队列负载机制、消息拉取机制、消息消费进度提交这三个非常重要的点，为后续的实践与问题排查打下坚实的基础。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="08&#32;消息消费&#32;API&#32;与版本变迁说明.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="10&#32;DefaultMQPushConsumer&#32;使用示例与注意事项.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434ad5cb6370ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
