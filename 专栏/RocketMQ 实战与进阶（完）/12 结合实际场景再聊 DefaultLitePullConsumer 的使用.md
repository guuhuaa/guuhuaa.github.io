<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>12 结合实际场景再聊 DefaultLitePullConsumer 的使用.md</title>
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

                    <a class="current-tab" href="12&#32;结合实际场景再聊&#32;DefaultLitePullConsumer&#32;的使用.md">12 结合实际场景再聊 DefaultLitePullConsumer 的使用.md</a>
                    

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
                        <div><h1>12 结合实际场景再聊 DefaultLitePullConsumer 的使用</h1>
<p>通过上文的讲解，各位读者朋友们应该对 DefaultLitePullConsumer 有了一个全面的理解，但会不会觉得意犹未尽之感，因为在实战环节只是给出了一个 Demo 级别的示例，本篇将一个大数据领域的消息拉取批处理场景丰富一些 DefaultLitePullConsumer 的使用技巧。</p>
<h3>场景描述</h3>
<p>现在订单系统会将消息发送到 ORDER_TOPIC 中，大数据这边需要将订单数据导入自己的计算平台，对用户、商家的订单行为进行分析。</p>
<h3>PUSH 与 PULL 模式选型</h3>
<p>大数据这边只需订阅 ORDER_TOPIC 主题就可以完成数据的同步，那是采用 PUSH 模式还是 PULL 模式呢？</p>
<p>大数据领域通常采用 PULL 模式，因为大数据数据计算都是基于 Spark 等批处理框架，基本都是批处理任务，例如每 5 分钟、每 10 分钟执行一次，而且一个批次能处理的数据越多越好，这样有利于大量数据分布式计算，整体性能计算效能更佳，如果采用 PUSH 模式，虽然也可以指定一次拉取的消息调试，但由于 PUSH 模式是几乎实时的，故每次拉取时服务端几乎不可能挤满了大量的消息，导致一次拉取的消息其实不多，再者是对于一个消费 JVM 来说，面对一个 RocketMQ 集群只会开启一条线程进行消息拉取，而 PULL 模式每一个消费者就可以指定多个消息拉取线程（默认为 20 个），故从消息拉取效能这个方面，PULL 模式占优，并且这个对实时性要求没那么高，故 综合考虑下来，该场景最终采用 PULL 模式。</p>
<h3>方案设计</h3>
<p>大概的实现思路如下图所示：</p>
<p><img src="assets/20200822122306949.png" alt="1" /></p>
<h3>代码实现与代码解读</h3>
<pre><code>// BigDataPullConsumer.java
package org.apache.rocketmq.example.simple.litepull;

import org.apache.rocketmq.client.consumer.DefaultLitePullConsumer;
import org.apache.rocketmq.client.producer.DefaultMQProducer;
import org.apache.rocketmq.common.consumer.ConsumeFromWhere;
import org.apache.rocketmq.common.message.MessageExt;
import org.apache.rocketmq.common.message.MessageQueue;
import org.apache.rocketmq.common.protocol.heartbeat.MessageModel;

import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.concurrent.*;
import java.util.stream.Collectors;

public class BigDataPullConsumer {

    private final ExecutorService executorService = new ThreadPoolExecutor(30, 30, 0L,
            TimeUnit.SECONDS, new ArrayBlockingQueue&lt;&gt;(10000), new DefaultThreadFactory(&quot;business-executer-
                                                                                        &quot;));

    private final ExecutorService pullTaskExecutor = new ThreadPoolExecutor(1, 1, 0L,
            TimeUnit.SECONDS, new ArrayBlockingQueue&lt;&gt;(10), new DefaultThreadFactory(&quot;pull-batch-&quot;));

    private String consumerGroup;
    private String nameserverAddr;
    private String topic;
    private String filter;
    private MessageListener messageListener;
    private DefaultMQProducer rertyMQProducer;
    private PullBatchTask pullBatchTask;

    public BigDataPullConsumer(String consumerGroup, String nameserverAddr, String topic, String filter) {
        this.consumerGroup = consumerGroup;
        this.nameserverAddr = nameserverAddr;
        this.topic = topic;
        this.filter = filter;
        initRetryMQProducer();
    }

    private void initRetryMQProducer() {
        this.rertyMQProducer = new DefaultMQProducer(consumerGroup + &quot;-retry&quot;);
        this.rertyMQProducer.setNamesrvAddr(this.nameserverAddr);
        try {
            this.rertyMQProducer.start();
        } catch (Throwable e) {
            throw new RuntimeException(&quot;启动失败&quot;, e);
        }

    }

    public void registerMessageListener(MessageListener messageListener) {
        this.messageListener = messageListener;
    }

    public void start() {
        //没有考虑重复调用问题
        this.pullBatchTask = new PullBatchTask(consumerGroup, nameserverAddr, topic,filter,messageListener);
        pullTaskExecutor.submit(this.pullBatchTask);
    }

    public void stop() {
        while(this.pullBatchTask.isRunning()) {
            try {
                Thread.sleep(1 * 1000);
            } catch (Throwable e) {
                //ignore
            }
        }
        this.pullBatchTask.stop();
        pullTaskExecutor.shutdown();
        executorService.shutdown();
        try {
            //等待重试任务结束
            while(executorService.awaitTermination(5, TimeUnit.SECONDS)) {
                this.rertyMQProducer.shutdown();
                break;
            }
        } catch (Throwable e) {
            //igonre
        }
    }

    /**
     * 任务监听
     */
    static interface MessageListener {
        boolean consumer(List&lt;MessageExt&gt; msgs);
    }

    /**
     * 定时调度任务，例如每 10 分钟会被调度一次
     */
    class PullBatchTask implements Runnable {
        DefaultLitePullConsumer consumer;
        String consumerGroup;
        String nameserverAddr;
        String topic;
        String filter;
        private volatile boolean running = true;
        private MessageListener messageListener;

        public PullBatchTask(String consumerGroup, String nameserverAddr,String topic, String filter, 
                             MessageListener messageListener) {
            this.consumerGroup = consumerGroup;
            this.nameserverAddr = nameserverAddr;
            this.topic = topic;
            this.filter = filter;
            this.messageListener = messageListener;
            init();
        }

        private void init() {
            System.out.println(&quot;init 方法被调用&quot;);
            consumer = new DefaultLitePullConsumer(this.consumerGroup);
            consumer.setNamesrvAddr(this.nameserverAddr);
            consumer.setAutoCommit(true);
            consumer.setMessageModel(MessageModel.CLUSTERING);
            consumer.setConsumeFromWhere(ConsumeFromWhere.CONSUME_FROM_FIRST_OFFSET);
            try {
                consumer.subscribe(topic, filter);
                consumer.start();
            } catch (Throwable e) {
                e.printStackTrace();
            }

        }

        public void stop() {
            this.running = false;
            this.consumer.shutdown();
        }

        public boolean isRunning() {
            return this.running;
        }

        @Override
        public void run() {
            this.running = true;
            long startTime = System.currentTimeMillis() - 5 * 1000;
            System.out.println(&quot;run 方法被调用&quot;);
            int notFoundMsgCount = 0;

            while(running) {
                try {
                    // 拉取一批消息
                    List&lt;MessageExt&gt; messageExts = consumer.poll();
                    if(messageExts != null &amp;&amp; !messageExts.isEmpty()) {
                        notFoundMsgCount = 0;//查询到数据，重置为 0；
                        // 使用一个业务线程池专门消费消息
                        try {
                            executorService.submit(new ExecuteTask(messageExts, messageListener));
                        } catch (RejectedExecutionException e) { //如果被拒绝，停止拉取，业务代码不去拉取，在
                            // RocketMQ 内部会最终也会触发限流，不会再拉取更多的消息，确保不会触发内存溢出。
                            boolean retry = true;
                            while (retry)
                            try {
                                Thread.sleep(5 * 1000);//简单的限流
                                executorService.submit(new ExecuteTask(messageExts, messageListener));
                                retry = false;
                            } catch (RejectedExecutionException e2) {
                                retry = true;
                            }
                        }

                        MessageExt last = messageExts.get(messageExts.size() - 1);
                        /**
                         * 如果消息处理的时间超过了该任务的启动时间，本次批处理就先结束
                         * 停掉该消费者之前，建议先暂停拉取，这样就不会从 broker 中拉取消息
                         * */
                        if(last.getStoreTimestamp() &gt; startTime) {
                            System.out.println(&quot;consumer.pause 方法将被调用。&quot;);
                            consumer.pause(buildMessageQueues(last));
                        }

                    } else {
                        notFoundMsgCount ++;
                    }

                    //如果连续出现 5 次未拉取到消息，说明本地缓存的消息全部处理，并且 pull 线程已经停止拉取了,此时可以结束本次消
                    //息拉取，等待下一次调度任务
                    if(notFoundMsgCount &gt; 5) {
                        System.out.println(&quot;已连续超过 5 次未拉取到消息，将退出本次调度&quot;);
                        break;
                    }
                } catch (Throwable e) {
                    e.printStackTrace();
                }
            }
            this.running = false;
        }

        /**
         * 构建 MessageQueue
         * @param msg
         * @return
         */
        private Set&lt;MessageQueue&gt; buildMessageQueues(MessageExt msg) {
            Set&lt;MessageQueue&gt; queues = new HashSet&lt;&gt;();
            MessageQueue queue = new MessageQueue(msg.getTopic(), msg.getBrokerName(), msg.getQueueId());
            queues.add(queue);
            return queues;
        }
    }

    /**
     * 任务执行
     */
    class ExecuteTask implements Runnable {
        private List&lt;MessageExt&gt; msgs;
        private MessageListener messageListener;
        public ExecuteTask(List&lt;MessageExt&gt; allMsgs, MessageListener messageListener) {
            this.msgs = allMsgs.stream().filter((MessageExt msg) -&gt; msg.getReconsumeTimes() &lt;= 
                                                16).collect(Collectors.toList());
            this.messageListener = messageListener;
        }
        @Override
        public void run() {
            try {
                 this.messageListener.consumer(this.msgs);
            } catch (Throwable e) {
                //消息消费失败，需要触发重试
                //这里可以参考 PUSH 模式，将消息再次发送到服务端。
                try {
                    for(MessageExt msg : this.msgs) {
                        msg.setReconsumeTimes(msg.getReconsumeTimes() + 1);
                        rertyMQProducer.send(msg);
                    }
                } catch (Throwable e2) {
                    e2.printStackTrace();
                    // todo 重试
                }
            }
        }
    }
}

// DefaultThreadFactory.java
package org.apache.rocketmq.example.simple.litepull;

import java.util.concurrent.ThreadFactory;
import java.util.concurrent.atomic.AtomicInteger;

public class DefaultThreadFactory implements ThreadFactory {
    private AtomicInteger num = new AtomicInteger(0);
    private String prefix;

    public DefaultThreadFactory(String prefix) {
        this.prefix = prefix;
    }

    @Override
    public Thread newThread(Runnable r) {
        Thread t = new Thread(r);
        t.setName(prefix + num.incrementAndGet());
        return t;
    }
}

// LitePullMain.java
package org.apache.rocketmq.example.simple.litepull;

import org.apache.rocketmq.common.message.MessageExt;

import java.util.List;
import java.util.concurrent.*;

public class LitePullMain {
    public static void main(String[] args) {

        String consumerGroup = &quot;dw_test_consumer_group&quot;;
        String nameserverAddr = &quot;192.168.3.166:9876&quot;;
        String topic = &quot;dw_test&quot;;
        String filter = &quot;*&quot;;
        /** 创建调度任务线程池 */
        ScheduledExecutorService schedule = new ScheduledThreadPoolExecutor(1, new 
                                                 DefaultThreadFactory(&quot;main-schdule-&quot;));
        schedule.scheduleWithFixedDelay(new Runnable() {
            @Override
            public void run() {
                BigDataPullConsumer demoMain = new BigDataPullConsumer(consumerGroup, nameserverAddr, topic, 
                                                                       filter);
                demoMain.registerMessageListener(new BigDataPullConsumer.MessageListener() {
                    /**
                     * 业务处理
                     * @param msgs
                     * @return
                     */
                    @Override
                    public boolean consumer(List&lt;MessageExt&gt; msgs) {
                        System.out.println(&quot;本次处理的消息条数：&quot; + msgs.size());
                        return true;
                    }
                });
                demoMain.start();
                demoMain.stop();
            }
        }, 1000, 30 * 1000, TimeUnit.MILLISECONDS);

        try {
            CountDownLatch cdh = new CountDownLatch(1);
            cdh.await(10 , TimeUnit.MINUTES);
            schedule.shutdown();
        } catch (Throwable e) {
            //ignore
        }

    }
}

</code></pre>
<p>程序运行结果如下图所示：</p>
<p><img src="assets/20200822122306955.png" alt="2" /></p>
<p>符合预期，可以看到两次调度，并且每一次调度都正常结束。</p>
<p>首先对各个类的职责做一个简单介绍：</p>
<ul>
<li>MessageListener：用来定义用户的消息处理逻辑。</li>
<li>PullBatchTask：使用 RocketMQ Lite Pull 消费者进行消息拉取的核心实现。</li>
<li>ExecuteTask：业务处理任务，在内部实现调用业务监听器，并执行重试相关的逻辑。</li>
<li>BigDataPullConsumer：本次业务的具体实现类</li>
<li>LitePullMain：本次测试主入口类。</li>
</ul>
<p>接下来对 PullBatchTask、ExecuteTask 的实现思路进行一个简单介绍，从而窥探一下消息 PULL 模式的一些使用要点。</p>
<p>PullBatchTask 的 run 方法主要是使用一个 while 循环，但通常不会用向 PUSH 模式实时监听，而是进行批量处理，即通过定时调度按批次进行处理，故需要有结束本次调度的逻辑，主要是为了提高消息拉取的效率，故本示例采用了本次任务启动只消费本次启动之前发送的消息，后面的新消息等聚集后在另一次调度时再消费，这里为了保证消费者停止时消息消费进度已经被持久化，这里并不会立即结束,而是在没有拉取合适的消息后调用 pause 方法暂停队列的消息，然后再连续多少次后并未拉取到消息后，在调用 DefaultLitePullConsumer 的 shutdown 方法，确保消息进度完整无误的提交到 Broker，从而避免大量消息重复消费。</p>
<p>消息消费端的业务处理这里引入了一个业务线程池，并且如果业务线程池积压，会触发消息拉取端的限流，从而避免内存溢出。</p>
<p>消息消费端在业务处理失败后，需要重试，将消息先发送到 Broker（主要的目的时方便消息消费进度向前推进）。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="11&#32;DefaultLitePullConsumer&#32;核心参数与实战.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="13&#32;结合实际场景顺序消费、消息过滤实战.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434aec0c2970ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
