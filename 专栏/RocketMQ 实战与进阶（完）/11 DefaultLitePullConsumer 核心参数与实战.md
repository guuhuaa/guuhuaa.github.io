<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>11 DefaultLitePullConsumer 核心参数与实战.md</title>
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

                    <a class="current-tab" href="11&#32;DefaultLitePullConsumer&#32;核心参数与实战.md">11 DefaultLitePullConsumer 核心参数与实战.md</a>
                    

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
                        <div><h1>11 DefaultLitePullConsumer 核心参数与实战</h1>
<p>在《消息消费 API 与版本变更》中也提到 DefaultMQPullConsumer（PULL 模式）的 API 太底层，使用起来及其不方便，RocketMQ 官方设计者也注意到这个问题，为此在 RocketMQ 4.6.0 版本中引入了 PULL 模式的另外一个实现类 DefaultLitePullConsumer，即从 4.6.0 版本后，DefaultMQPullConsumer 已经被标记为废弃，故接下来将重点介绍 DefaultLitePullConsumer，并探究如何在实际中运用它解决相关问题。</p>
<h3>DefaultLitePullConsumer 类图</h3>
<p>首先我们来看一下 DefaultLitePullConsumer 的类图结构，如下图所示：</p>
<p><img src="assets/2020081719084658.png" alt="1" /></p>
<h4><strong>核心方法详解</strong></h4>
<p>核心方法说明如下。</p>
<pre><code>void start()

</code></pre>
<p>启动消费者。</p>
<pre><code>void shutdown()

</code></pre>
<p>关闭消费者。</p>
<pre><code>void subscribe(String topic, String subExpression)

</code></pre>
<p>按照主题与消息过滤表达式进行订阅。</p>
<pre><code>void subscribe(String topic, MessageSelector selector)

</code></pre>
<p>按照主题与过滤表达式订阅消息，过滤表达式可通过 MessageSelector 的 bySql、byTag 来创建，这个与 PUSH 模式类似，故不重复展开。</p>
<blockquote>
<p>温馨提示：通过 subscribe 方式订阅 Topic，具备消息消费队列的重平衡，即如果消费消费者数量、主题的队列数发生变化时，各个消费者订阅的队列信息会动态变化。</p>
</blockquote>
<pre><code>void unsubscribe(String topic)

</code></pre>
<p>取消订阅。</p>
<pre><code>void assign(Collection&lt; MessageQueue &gt; messageQueues)

</code></pre>
<p>收到指定该消费者消费的队列，这种消费模式不具备消息消费队列的自动重平衡。</p>
<pre><code>List&lt;MessageExt&gt; poll()

</code></pre>
<p>消息拉取 API，默认超时时间为 5s。</p>
<pre><code>List&lt;MessageExt&gt; poll(long timeout)

</code></pre>
<p>消息拉取 API，可指定消息拉取超时时间。在学习中笔者通常喜欢进行对比学习，故我们不妨对比一下 DefaultMQPullConsumer 的 pull 方法。</p>
<p><img src="assets/20200817190858266.png" alt="2" /></p>
<p>可以看出 LIte Pull Consumer 的拉取风格发生了变化，不需要用户手动指定队列拉取，而是通过订阅或指定队列，然后自动根据位点进行消息拉取，显得更加方便，个人觉得 DefaultLitePullConsumer 相关的 API 有点类似 Kafka 的工作模式了。</p>
<pre><code>void seek(MessageQueue messageQueue, long offset)

</code></pre>
<p>改变下一次消息拉取的偏移量，即改变 poll() 方法下一次运行的拉取消息偏移量，类似于回溯或跳过消息，注意：如果设置的 offset 大于当前消费队列的消费偏移量，就会造成部分消息直接跳过没有消费，使用时请慎重。</p>
<pre><code>void seekToBegin(MessageQueue messageQueue)

</code></pre>
<p>改变下一次消息拉取的偏移量到消息队列最小偏移量。其效果相当于重新来过一次。</p>
<pre><code>void seekToEnd(MessageQueue messageQueue)

</code></pre>
<p>该变下一次消息拉取偏移量到队列的最大偏移量，即跳过当前所有的消息，从最新的偏移量开始消费。</p>
<pre><code>void pause(Collection&lt; MessageQueue &gt; messageQueues)

</code></pre>
<p>暂停消费，支持将某些消息消费队列挂起，即 poll() 方法在下一次拉取消息时会暂时忽略这部分消息消费队列，可用于消费端的限流。</p>
<pre><code>void resume(Collection&lt; MessageQueue &gt; messageQueues)

</code></pre>
<p>恢复消费。</p>
<pre><code>boolean isAutoCommit()

</code></pre>
<p>是否自动提交消费位点，Lite Pull 模式下可设置是否自动提交位点。</p>
<pre><code>void setAutoCommit(boolean autoCommit)

</code></pre>
<p>设置是否自动提交位点。</p>
<pre><code>Collection&lt;MessageQueue&gt; fetchMessageQueues(String topic)

</code></pre>
<p>获取 Topic 的路由信息。</p>
<pre><code>Long offsetForTimestamp(MessageQueue messageQueue, Long timestamp)

</code></pre>
<p>根据时间戳查找最接近该时间戳的消息偏移量。</p>
<pre><code>void commitSync()

</code></pre>
<p>手动提交消息消费位点，在集群消费模式下，调用该方法只是将消息偏移量提交到 OffsetStore 在内存中，并不是实时向 Broker 提交位点，位点的提交还是按照定时任务定时向 Broker 汇报。</p>
<pre><code>Long committed(MessageQueue messageQueue)

</code></pre>
<p>获取该消息消费队列已提交的消费位点（从 OffsetStore 中获取，即集群模式下会向 Broker 中的消息消费进度文件中获取。</p>
<pre><code>void registerTopicMessageQueueChangeListener(String topic,TopicMessageQueueChangeListener listener)

</code></pre>
<p>注册主题队列变化事件监听器，客户端会每 30s 查询一下 订阅的 Topic 的路由信息（队列信息）的变化情况，如果发生变化，会调用注册的事件监听器。关于 TopicMessageQueueChangeListener 事件监听器说明如下：</p>
<p><img src="assets/20200817190908682.png" alt="3" /></p>
<p>事件监听参数说明如下。</p>
<pre><code>String topic

</code></pre>
<p>主题名称。</p>
<pre><code>Set&lt;MessageQueue&gt; messageQueues

</code></pre>
<p>当前该 Topic 所有的队列信息。</p>
<pre><code>void updateNameServerAddress(String nameServerAddress)

</code></pre>
<p>更新 NameServer 的地址。</p>
<h4><strong>核心属性介绍</strong></h4>
<p>通过对 DefaultLitePullConsumer 核心方法的了解，再结合我们目前已掌握的 DefaultMQPullConsumer、DefaultMQPushConsumer 相关知识，我相信大家对如何使用 DefaultLitePullConsumer 显得胸有成竹了，故暂时先不进入实战，我们一鼓作气看一下其核心属性。</p>
<pre><code>String consumerGroup

</code></pre>
<p>消息消费组。</p>
<pre><code>long brokerSuspendMaxTimeMillis

</code></pre>
<p>长轮询模式，如果开启长轮询模式，当 Broker 收到客户端的消息拉取请求时如果当时并没有新的消息，可以在 Broker 端挂起当前请求，一旦新消息到达则唤醒线程，从 Broker 端拉取消息后返回给客户端，该值设置在 Broker 等待的最大超时时间，默认为 20s，建议保持默认值即可。</p>
<pre><code>long consumerTimeoutMillisWhenSuspend

</code></pre>
<p>消息消费者拉取消息最大的超时时间，该值必须大于 brokerSuspendMaxTimeMillis，默认值为 30s，同样不建议修改该值。</p>
<pre><code>long consumerPullTimeoutMillis

</code></pre>
<p>客户端与 Broker 建立网络连接的最大超时时间，默认为 10s。</p>
<pre><code>MessageModel messageModel

</code></pre>
<p>消息组消费模型，可选值：集群模式、广播模式。</p>
<pre><code>MessageQueueListener messageQueueListener

</code></pre>
<p>消息消费负载队列变更事件。</p>
<pre><code>OffsetStore offsetStore

</code></pre>
<p>消息消费进度存储器，与 PUSH 模式机制一样。</p>
<pre><code>AllocateMessageQueueStrategy allocateMessageQueueStrategy

</code></pre>
<p>消息消费队列负载策略，与 PUSH 模式机制一样。</p>
<pre><code>boolean autoCommit

</code></pre>
<p>设置是否提交消息消费进度，默认为 true。</p>
<pre><code>int pullThreadNums

</code></pre>
<p>消息拉取线程数量，默认为 20 个，注意这个是每一个消费者默认 20 个线程往 Broker 拉取消息。<strong>这个应该是 Lite PULL 模式对比 PUSH 模式一个非常大的优势。</strong></p>
<pre><code>long autoCommitIntervalMillis

</code></pre>
<p>自动汇报消息位点的间隔时间，默认为 5s。</p>
<pre><code>int pullBatchSize

</code></pre>
<p>一次消息拉取最多返回的消息条数，默认为 10。</p>
<pre><code>int pullThresholdForQueue

</code></pre>
<p>对于单个队列挤压的消息条数触发限流的阔值，默认为 1000，即如果某一个队列在本地挤压超过 1000 条消息，则停止消息拉取。</p>
<pre><code>int pullThresholdSizeForQueue

</code></pre>
<p>对于单个队列挤压的消息总大小触发限流的阔值，默认为 100M。</p>
<pre><code>int consumeMaxSpan

</code></pre>
<p>单个消息处理队列中最大消息偏移量与最小偏移量的差值触发限流的阔值，默认为 2000。</p>
<pre><code>long pullThresholdForAll

</code></pre>
<p>针对所有队列的消息消费请求数触发限流的阔值，默认为 10000。</p>
<pre><code>long pollTimeoutMillis

</code></pre>
<p>一次消息拉取默认的超时时间为 5s。</p>
<pre><code>long topicMetadataCheckIntervalMillis

</code></pre>
<p>topic 路由信息更新频率，默认 30s 更新一次。</p>
<pre><code>ConsumeFromWhere consumeFromWhere

</code></pre>
<p>初次启动时从什么位置开始消费，同 PUSH 模式。</p>
<pre><code>String consumeTimestamp

</code></pre>
<p>如果初次启动时 consumeFromWhere 策略选择为基于时间戳，通过该属性设置定位的时间，同 PUSH 模式。</p>
<h3>DefaultLitePullConsumer 简单使用示例</h3>
<p>介绍了 DefaultLitePullConsumer 的方法与核心属性后，我们先来运用其 API 完成 Demo 程序的调试，在下一篇文章中将会结合应用场景再进一步学习使用 DefaultLitePullConsumer，示例代码如下：</p>
<pre><code>public class LitePullConsumerSubscribe02 {
    public static volatile boolean running = true;
    public static void main(String[] args) throws Exception {
        DefaultLitePullConsumer litePullConsumer = new 
            DefaultLitePullConsumer(&quot;dw_lite_pull_consumer_test&quot;);
        litePullConsumer.setNamesrvAddr(&quot;192.168.3.166:9876&quot;);
        litePullConsumer.setConsumeFromWhere(ConsumeFromWhere.CONSUME_FROM_FIRST_OFFSET);
        litePullConsumer.subscribe(&quot;TopicTest&quot;, &quot;*&quot;);
        litePullConsumer.setAutoCommit(true); //该值默认为 true
        litePullConsumer.start();
        try {
            while (running) {
                List&lt;MessageExt&gt; messageExts = litePullConsumer.poll();
                doConsumeSomething(messageExts);
            }
        } finally {
            litePullConsumer.shutdown();
        }
    }
    private static void doConsumeSomething(List&lt;MessageExt&gt; messageExts) {
        // 真正的业务处理
        System.out.printf(&quot;%s%n&quot;, messageExts);
    }
}

</code></pre>
<p>上面的示例是基于自动提交消息消费进度的，如果采取手动提交，需要应用程序手动调用 consumer 的 commitSync() 方法，乍一看，大家是不是觉得 Lite Pull 模式并且采用自动提交消费位点与 PUSH 模式差别不大，那果真如此吗？接下来我们来对比一下 Lite Pull 与 PUSH 模式的异同。</p>
<h3>Lite Pull 与 PUSH 模式之对比</h3>
<p>从上面的示例可以看出 Lite PULL 相关的 API 比 4.6.0 之前的 DefaultMQPullConsumer 的使用上要简便不少，从编程风格上已非常接近了 PUSH 模式，其底层的实现原理是否也一致呢？显然不是的，请听我我慢慢道来。</p>
<p>不知大家是否注意到，Lite PULL 模式下只是通过 poll() 方法拉取一批消息，然后提交给应用程序处理，**采取自动提交模式下位点的提交与消费结果并没有直接挂钩，即消息如果处理失败，其消费位点还是继续向前继续推进，缺乏消息的重试机制。**为了论证笔者的观点，这里给出 DefaultLitePullConsumer 的 poll() 方法执行流程图，请大家重点关注位点提交所处的位置。</p>
<p><img src="assets/20200817190919223.png" alt="4" /></p>
<p><strong>Lite Pull 模式的自动提交位点，一个非常重要的特征是 poll() 方法一返回，这批消息就默认是消费成功了</strong>，一旦没有处理好，就会造成消息丢失，那有没有方法解决上述这个问题呢，<strong>seek 方法就闪亮登场了</strong>，在业务方法处理过程中，如果处理失败，可以通过 seek 方法重置消费位点，即在捕获到消息业务处理后，需要根据返回的第一条消息中（MessageExt）信息构建一个 MessageQueue 对象以及需要重置的位点。</p>
<p>Lite Pull 模式的消费者相比 PUSH 模式的另外一个不同点事 Lite Pull 模式没有消息消费重试机制，PUSH 模式在并发消费模式下默认提供了 16 次重试，并且每一次重试的间隔不一致，极大的简化了编程模型。在这方面 Lite Pull 模型还是会稍显复杂。</p>
<p>Lite Pull 模式针对 PUSH 模式一个非常大亮点是消息拉取线程是以消息消费组为维度的，而且一个消费者默认会创建 20 个拉取任务，在消息拉取效率方面比 PUSH 模型具有无可比拟的优势，特别适合大数据领域的批处理任务，即每隔多久运行一次的拉取任务。</p>
<h3>长轮询实现原理</h3>
<p>PULL 模式通常适合大数据领域的批处理操作，对消息的实时性要求不高，更加看重的是消息的拉取效率，即一次消息需要拉取尽可能多的消息，这样方便一次性对大量数据进行处理，提高数据的处理效率，特别是希望一次消息拉取再不济也要拉取点消息，不要出现太多无效的拉取请求（没有返回消息的拉取请求）。</p>
<p>首先大家来看一下如下这个场景：</p>
<p><img src="assets/20200817190929584.png" alt="5" /></p>
<p>即 Broker 端没有新消息时，Broker 端采取何种措施呢？我想基本有如下两种策略进行选择：</p>
<ul>
<li>Broker 端没有新消息，立即返回，拉取结果中不包含任何消息。</li>
<li>当前拉取请求在 Broker 端挂起，在 Broker 端挂起，并且轮询 Broker 端是否有新消息，即轮询机制。</li>
</ul>
<p>上面说的第二种方式，有一个“高大上”的名字——<strong>轮询</strong>，根据轮询的方式又可以分为<strong>长轮询、短轮询</strong>。</p>
<ul>
<li><strong>短轮询</strong>：第一次未拉取到消息后等待一个时间间隔后再试，默认为 1s，可以在 Broker 的配置文件中设置 shortPollingTimeMills 改变默认值，即轮询一次，<strong>注意：只轮询一次</strong>。</li>
<li><strong>长轮询</strong>：可以由 PULL 客户端设置在 Broker 端挂起的超时时间，默认为 20s，然后在 Broker 端没有拉取到消息后默认每隔 5s 一次轮询，并且在 Broker 端获取到新消息后，会唤醒拉取线程，结束轮询，尝试一次消息拉取，然后返回一批消息到客户端，长轮询的时序图如下所示：</li>
</ul>
<p><img src="assets/20200817190938839.png" alt="6" /></p>
<p>从这里可以看出，长轮询比短轮询，轮询等待的时间长，短轮询只轮询一次，并且默认等待时间为 1s，而长轮询默认一次阻塞 5s，但支持被唤醒。</p>
<p>在 broker 端与长轮询相关的参数如下：</p>
<ul>
<li>longPollingEnable：是否开启长轮询，默认为 true。</li>
<li>shortPollingTimeMills：短轮询等待的时间，默认为 1000，表示 1s。</li>
</ul>
<h3>小结</h3>
<p>本篇详细介绍了 RocketMQ 于 4.6.0 版本引入的新版 PULL 模式消息者实现类核心方法与核心属性，并给出简单的使用示例，然后重点总结了 Lite Pull 与 PUSH 模式的差异，并思考其使用场景，最后总结了一下消息拉取模式中一个非常重要的机制——长轮询机制，一次消息拉取尽可能拉取到消息做最大努力。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="10&#32;DefaultMQPushConsumer&#32;使用示例与注意事项.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="12&#32;结合实际场景再聊&#32;DefaultLitePullConsumer&#32;的使用.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434ae7286c70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
