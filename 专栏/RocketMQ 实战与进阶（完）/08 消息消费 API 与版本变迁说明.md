<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>08 消息消费 API 与版本变迁说明.md</title>
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

                    <a class="current-tab" href="08&#32;消息消费&#32;API&#32;与版本变迁说明.md">08 消息消费 API 与版本变迁说明.md</a>
                    

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
                        <div><h1>08 消息消费 API 与版本变迁说明</h1>
<p>从本篇开始我们将详细介绍 RockeMQ 的消息消费端的 API。</p>
<h3>消息消费类图</h3>
<p>RocketMQ 消费端的 API 如下图所示：</p>
<p><img src="assets/20200811225030941.png" alt="1" /></p>
<p>其核心类图如下所示。</p>
<p><strong>MQAdmin</strong></p>
<p>MQ 一些基本的管理功能，例如创建 Topic，这里稍微有点奇怪，消费端应该不需要继承该接口。该类在消息发送 API 章节已详细介绍，再次不再重复说明。</p>
<p><strong>MQConsumer</strong></p>
<p>MQ 消费者，这个接口定义得过于简单，如果该接口需要，可以将其子接口一些共同的方法提取到该接口中。</p>
<pre><code>Set&lt;MessageQueue&gt; fetchSubscribeMessageQueues(final String topic)

</code></pre>
<p>获取分配该 Topic 所有的读队列。</p>
<p><strong>MQPushConsumer</strong></p>
<p>RocketMQ 支持推、拉两种模式，该接口是<strong>拉模式</strong>的接口定义。</p>
<pre><code>void start()

</code></pre>
<p>启动消费者。</p>
<pre><code>void shutdown()

</code></pre>
<p>关闭消费者。</p>
<pre><code>void registerMessageQueueListener(String topic, MessageQueueListener listener)

</code></pre>
<p>注册消息队列变更回调时间，即消费端分配到的队列发生变化时触发的回调函数，其声明如下：</p>
<p><img src="assets/2020081122504049.png" alt="2" /></p>
<p>其参数说明如下：</p>
<ul>
<li><code>String topic</code>：主题。</li>
<li><code>Set&lt;MessageQueue&gt; mqAll</code>：该 Topic 所有的队列集合。</li>
<li><code>Set&lt;MessageQueue&gt; mqDivided</code>：分配给当前消费者的消费队列。</li>
</ul>
<pre><code>PullResult pull(MessageQueue mq, String subExpression, long offset,int maxNums, long timeout)

</code></pre>
<p>消息拉取，应用程序可以通过调用该方法从 RocketMQ 服务器拉取一篇消息，其参数含义说明如下：</p>
<ul>
<li><code>MessageQueue mq</code>：消息消费队列。</li>
<li><code>String subExpression</code>：消息过滤表达式，基于 Tag、SQL92 的过滤表达式。</li>
<li><code>long offset</code>：消息偏移量，消息在 ConsumeQueue 中的偏移量。</li>
<li><code>int maxNums</code>：一次消息拉取返回的最大消息条数。</li>
<li><code>long timeout</code>：本次拉取的超时时间。</li>
</ul>
<pre><code>PullResult pull(MessageQueue mq, MessageSelector selector, long offset,int maxNums, long timeout)

</code></pre>
<p>pull 重载方法，通过 MessageSelector 构建消息过滤对象，可以通过 MessageSelector 的 buildSql、buildTag 两个方法构建过滤表达式。</p>
<pre><code>void pull(MessageQueue mq, String subExpression, long offset, int maxNums,PullCallback pullCallback)

</code></pre>
<p>异步拉取，调用其异步回调函数 PullCallback。</p>
<pre><code>PullResult pullBlockIfNotFound(MessageQueue mq, String subExpression,long offset, int maxNums)

</code></pre>
<p>拉取消息，如果服务端没有新消息待拉取，一直阻塞等待，直到有消息返回，同样该方法有一个重载放假支持异步拉取。</p>
<pre><code>void updateConsumeOffset(MessageQueue mq, long offset)

</code></pre>
<p>更新消息消费处理进度。</p>
<pre><code>long fetchConsumeOffset(MessageQueue mq, boolean fromStore)

</code></pre>
<p>获取指定消息消费队列的消费进度。其中参数 fromStore 如果为 true，表示从消息消费进度存储文件中获取消费进度。</p>
<pre><code>Set&lt;MessageQueue&gt; fetchMessageQueuesInBalance(String topic)

</code></pre>
<p>获取当前正在处理的消息消费队列（通过消息队列负载机制分配的队列）。</p>
<pre><code>void sendMessageBack(MessageExt msg, int delayLevel, String brokerName, String consumerGroup)

</code></pre>
<p>消息消费失败后发送的 ACK。</p>
<p><strong>MQPushConsumer</strong></p>
<p>RocketMQ <strong>推模式</strong>消费者接口。</p>
<pre><code>void start()

</code></pre>
<p>启动消费者。</p>
<pre><code>void shutdown()

</code></pre>
<p>关闭消费者。</p>
<pre><code>void registerMessageListener(MessageListenerConcurrently messageListener)

</code></pre>
<p>注册并发消费模式监听器。</p>
<pre><code>void registerMessageListener(MessageListenerOrderly messageListener)

</code></pre>
<p>注册顺序消费模式监听器。</p>
<pre><code>void subscribe(String topic, String subExpression)

</code></pre>
<p>订阅主题。其参数说明如下：</p>
<ul>
<li><code>String topic</code>： 订阅的主题，RocketMQ 支持一个消费者订阅多个主题，操作方式是多次调用该方法。</li>
<li><code>String subExpression</code>：消息过滤表达式，例如传入订阅的 tag，SQL92 表达式。</li>
</ul>
<pre><code>void subscribe(String topic, MessageSelector selector)

</code></pre>
<p>订阅主题，重载方法，MessageSelector 提供了 buildSQL、buildTag 的订阅方式。</p>
<pre><code>void unsubscribe(String topic)

</code></pre>
<p>取消订阅。</p>
<pre><code>void suspend()

</code></pre>
<p>挂起消费。</p>
<pre><code>void resume()

</code></pre>
<p>恢复继续消费。</p>
<p><strong>DefaultMQPushConsumer</strong></p>
<p>RocketMQ 消息推模式默认实现类。</p>
<p><strong>DefaultMQPullConsumer</strong></p>
<p>RocketMQ 消息拉取模式默认实现类。</p>
<p>在 RocketMQ 的内部实现原理中，其实现机制为 PULL 模式，而 PUSH 模式是一种伪推送，是对 PULL 模式的封装，PUSH 模式的实现原理如下图所示：</p>
<p><img src="assets/2020081122504049.png" alt="3" /></p>
<p>即 PUSH 模式就是对 PULL 模式的封装，每拉去一批消息后，提交到消费端的线程池（异步），然后马上向 Broker 拉取消息，即实现类似“推”的效果。</p>
<p>从 PULL 模式来看，消息的消费主要包含如下几个方面：</p>
<ul>
<li>消息拉取，消息拉取模式通过 PULL 相关的 API 从 Broker 指定消息消费队列中拉取一批消息到消费消费客户端，多个消费者需要手动完成队列的分配。</li>
<li>消息消费端处理完消费，需要向 Broker 端报告消息处理队列，然后继续拉取下一批消息。</li>
<li>如果遇到消息消费失败，需要告知 Broker，该条消息消费失败，后续需要重试，通过手动调用 sendMessageBack 方法实现。</li>
</ul>
<p>而 PUSH 模式就上述这些处理操作无需使用者考虑，只需告诉 RocketMQ 消费者在拉取消息后需要调用的事件监听器即可，消息消费进度的存储、消息消费的重试统一由 RocketMQ Client 来实现。</p>
<h3>消息消费 API 简单使用示例</h3>
<p>从上文基本可以得知，推模式 API 与拉模式 API 在使用层面的差别，可以简单理解为汽车领域的自动挡与手动挡。在实际业务类场景中，通常使用的是推送风格的 API，适合实时监控；但在大数据领域，通常是跑批处理即定时类任务，故大数据领域通常使用拉模式更多。</p>
<p>接下来编写几个示例代码对拉取、推送相关 API 进行一个使用方面的演示。</p>
<h4><strong>RocketMQ 拉模式核心 API 使用示例</strong></h4>
<p>使用场景：例如公司大数据团队需要对订单进行分析，为了提高计算效能，采取每 2 个小时调度一次，每批任务处理任务启动之前的所有消息。</p>
<p>首先我先给出一个基于 RocketMQ PULL 的 API 的编程示例代码，本示例接近生产实践，示例代码如下：</p>
<pre><code>import org.apache.rocketmq.client.consumer.DefaultMQPullConsumer;
import org.apache.rocketmq.client.consumer.PullResult;
import org.apache.rocketmq.common.message.MessageExt;
import org.apache.rocketmq.common.message.MessageQueue;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.TimeUnit;
public class PullConsumerTest {
    public static void main(String[] args) throws Exception {
        Semaphore semaphore = new Semaphore();
        Thread t = new Thread(new Task(semaphore));
        t.start();
        CountDownLatch cdh = new CountDownLatch(1);
        try {
            //程序运行 120s　后介绍
            cdh.await(120 * 1000, TimeUnit.MILLISECONDS);
        } finally {
            semaphore.running = false;
        }
    }
    /**
     * 消息拉取核心实现逻辑
     */
    static class Task implements Runnable {
        Semaphore s = new Semaphore();
        public Task(Semaphore s ) {
            this.s = s;
        }
        public void run() {
            try {
                DefaultMQPullConsumer consumer = new 
                    DefaultMQPullConsumer(&quot;dw_pull_consumer&quot;);
                consumer.setNamesrvAddr(&quot;127.0.01:9876&quot;);
                consumer.start();
                Map&lt;MessageQueue, Long&gt; offsetTable = new HashMap&lt;MessageQueue, Long&gt;();
                Set&lt;MessageQueue&gt; msgQueueList = consumer.
                    fetchSubscribeMessageQueues(&quot;TOPIC_TEST&quot;); // 获取该 Topic 的所有队列
                if(msgQueueList != null &amp;&amp; !msgQueueList.isEmpty()) {
                    boolean noFoundFlag = false;
                    while(this.s.running) {
                        if(noFoundFlag) { //　没有找到消息，暂停一下消费
                            Thread.sleep(1000);
                        }
                        for( MessageQueue q : msgQueueList ) {
                            PullResult pullResult = consumer.pull(q, &quot;*&quot;,                                          decivedPulloffset(offsetTable
                             , q, consumer) , 3000);
                            System.out.println(&quot;pullStatus:&quot; + 
                                               pullResult.getPullStatus());
                            switch (pullResult.getPullStatus()) {
                                case FOUND:
                                    doSomething(pullResult.getMsgFoundList());
                                    break;
                                case NO_MATCHED_MSG:
                                    break;
                                case NO_NEW_MSG:
                                case OFFSET_ILLEGAL:
                                    noFoundFlag = true;
                                    break;
                                default:
                                    continue ;
                            }
                            //提交位点
                            consumer.updateConsumeOffset(q, 
                                 pullResult.getNextBeginOffset());
                        }
                        System.out.println(&quot;balacne queue is empty: &quot; + consumer.
                              fetchMessageQueuesInBalance(&quot;TOPIC_TEST&quot;).isEmpty());
                    }
                } else {
                    System.out.println(&quot;end,because queue is enmpty&quot;);
                }
                consumer.shutdown();
                System.out.println(&quot;consumer shutdown&quot;);
            } catch (Throwable e) {
                e.printStackTrace();
            }
        }
    }
    /** 拉取到消息后具体的处理逻辑　*/
    private static void doSomething(List&lt;MessageExt&gt; msgs) {
        System.out.println(&quot;本次拉取到的消息条数:&quot; + msgs.size());
    }
    public static long decivedPulloffset(Map&lt;MessageQueue, Long&gt; offsetTable, 
             MessageQueue queue, DefaultMQPullConsumer consumer) throws Exception {
        long offset = consumer.fetchConsumeOffset(queue, false);
        if(offset &lt; 0 ) {
            offset = 0;
        }
        System.out.println(&quot;offset:&quot; + offset);
        return offset;
    }
    static class Semaphore {
        public volatile boolean running = true;
    }
}

</code></pre>
<p>关于上述代码，提供了优雅的线程拉取的方法，消息的拉取实现主要在任务 Task 的 run 方法中，主要的实现技巧如下：</p>
<ul>
<li>首先根据 MQConsumer 的 fetchSubscribeMessageQueues 的方法获取 Topic 的所有队列信息。</li>
<li>然后遍历所有队列，依次通过 MQConsuemr 的 PULL 方法从 Broker 端拉取消息。</li>
<li>对拉取的消息进行消费处理。</li>
<li>通过调用 MQConsumer 的 updateConsumeOffset 方法更新位点，但需要注意的是这个方法并不是实时向 Broker 提交，而是客户端会启用以线程，默认每隔 5s 向 Broker 集中上报一次。</li>
</ul>
<p>上面的示例演示的是一个消费组只有一个消费者，如果有多个消费组呢？这里就涉及到队列的重新分配，而每一个消费者是否只负责拉取分配的队列，是不是觉得这个直接使用 PULL 模式，是不是觉得有点复杂了。笔者也觉得是，接下来我们来看一下 PUSH 模式。</p>
<h4><strong>RocketMQ 推模式使用示例</strong></h4>
<p>在 RocketMQ 中绝大数场景中，通常会选择使用 PUSH 模式，因为 PUSH 模式是对 PULL 模式的封装，将消息的拉取、消息队列的自动负载、消息进度（位点）自动提交、消息消费重试都进行了封装，无需使用者关心，其示例代码如下：</p>
<pre><code>public static void main(String[] args) throws InterruptedException, MQClientException {
        DefaultMQPushConsumer consumer = new 
            DefaultMQPushConsumer(&quot;dw_test_consumer_6&quot;);
        consumer.setNamesrvAddr(&quot;127.0.0.1:9876&quot;);
        consumer.setConsumeFromWhere(ConsumeFromWhere.CONSUME_FROM_FIRST_OFFSET);
        consumer.subscribe(&quot;TOPIC_TEST&quot;, &quot;*&quot;);
        consumer.setAllocateMessageQueueStrategy(new 
               AllocateMessageQueueAveragelyByCircle());
        consumer.registerMessageListener(new MessageListenerConcurrently() {
            @Override
            public ConsumeConcurrentlyStatus consumeMessage(List&lt;MessageExt&gt; msgs,
                ConsumeConcurrentlyContext context) {
                try {
                    System.out.printf(&quot;%s Receive New Messages: %s %n&quot;, 
                          Thread.currentThread().getName(), msgs);
                    return ConsumeConcurrentlyStatus.CONSUME_SUCCESS;
                } catch (Throwable e) {
                    e.printStackTrace();
                    return ConsumeConcurrentlyStatus.RECONSUME_LATER;
                }
            }
        });
        consumer.start();
        System.out.printf(&quot;Consumer Started.%n&quot;);
    }

</code></pre>
<p>上面的代码是不是非常简单。在后续的文章我们会重点对 PUSH 模式消费者的核心属性即工作原理做详细的介绍。使用 DefaultMQPushConsumer 开发一个消费者，其代码基本覆盖如下几个方面：</p>
<ul>
<li>首先 new DefaultMQPushConsumer 对象，并指定一个消费组名。</li>
<li>然后设置相关参数，例如 nameSrvAdd、消费失败重试次数、线程数等（可以设置哪些参数将在下篇文章中详细介绍）。</li>
<li>通过调用 setConsumeFromWhere 方法指定初次启动时从什么地方消费，默认是最新的消息开始消费。</li>
<li>通过调用 setAllocateMessageQueueStrategy 指定队列负载机制，默认平均分配。</li>
<li>通过调用 registerMessageListener 设置消息监听器，即消息处理逻辑，最终返回 CONSUME_SUCCESS（成功消费）或 RECONSUME_LATER（需要重试）。</li>
</ul>
<blockquote>
<p>温馨提示，关于消息消费的详细使用，将在后面的文章中进行详细介绍。</p>
</blockquote>
<h3>消息消费 API 版本演变说明</h3>
<p>RocketMQ 在消费端的 API 相对来说还是比较稳定的，只是在 RocketMQ 4.6.0 版本引入了 DefaultLitePullConsumer，如果上述 PULL 示例代码引用的 Client 包版本为 4.6.0，细心的读者朋友们肯定会发现 DefaultMQPullConsumer 已过期，取代它的正是 DefaultLitePullConsumer。那这是什么原因呢？</p>
<p>我想只要大家使用过 DefaultMQPullConsumer 编写代码后，就会发现这个类的 API 太底层，使用者需要考虑的问题太多，例如队列负载、消费进度存储等等方面，可以毫不夸张地说，要用好 DefaultMQPullConsumer 还是不那么容易的。</p>
<p>RocketMQ 设计者也意识到了这样的问题，故引入了 DefaultLitePullConsumer，按照官方文档上的介绍，该类具备如下特性：</p>
<ul>
<li>支持以订阅方式进行消息消费，支持消费队列自动再平衡。</li>
<li>支持手动分配队列的方式进行消息消费，此模式不支持队列自动再平衡。</li>
<li>提供 seek/commit 方法来重置、提交消费位点。</li>
</ul>
<p>温馨提示：由于 DefaultLitePullConsumer 的内容比较多，我们将在后续单独一篇文章对其参数、方法、使用示例进行详细介绍，故本篇只是告知其引入的目的。</p>
<h3>小结</h3>
<p>本篇详细介绍了 RocketMQ PUSH、PULl 两种消息消费模式的核心 API，并对相关 API 进行了演示，后续会详细结合实际场景，并梳理核心参数，给出使用建议，后面引出了 RocketMQ 消费者一个重大的版本变更。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="07&#32;事务消息使用及方案选型思考.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="09&#32;DefaultMQPushConsumer&#32;核心参数与工作原理.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434ad05d7c70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
