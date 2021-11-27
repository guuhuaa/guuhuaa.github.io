<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>20 RocketMQ 集群监控（二）.md</title>
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

                    <a class="current-tab" href="20&#32;RocketMQ&#32;集群监控（二）.md">20 RocketMQ 集群监控（二）.md</a>
                    

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
                        <div><h1>20 RocketMQ 集群监控（二）</h1>
<h3>前言</h3>
<p>主题和消费组通常使用方比较关心的资源，发送方关注主题，消费方关注消费组。管理员更侧重关注集群的健康状况。本文介绍主题和消费组的监控实战，包括监控项的设计、及每个监控项的代码实现。</p>
<h3>监控项设计</h3>
<p>我们先把主题监控和消费监控统称为资源监控，下图分列了主题和消费组包含的监控项。</p>
<p><img src="assets/20200827092950837.png" alt="img" /></p>
<h4><strong>主题监控</strong></h4>
<p>从发送速度、发送耗时、消息大小、日消息量方面整理主题监控项，下面分别介绍这些监控项的重要性。</p>
<p><strong>发送速度</strong></p>
<p>通过实时采集主题的发送速度，来掌握主题的流量情况。例如：有些业务场景不允许主题的发送速度掉为 0，那通过实时采集发送速度指标，为将来告警做准备。</p>
<p><strong>发送变化率</strong></p>
<p>发送变化率是指，特定时间内主题的发送速度变化了多少。例如：5 分钟内发送速率陡增了 2 倍。通常用于两方面，一个是保护集群，某个 Topic 过高的瞬时流量可能对集群安全造成影响。例如：一个发送速率为 5000 的主题，在 3 分钟内陡增了 5 倍，到了 25000 的高度，这种流量对集群存在安全隐患。另一个是使用角度检测业务是否正常，比如一个发送速率为 8000 的主题，在 3 分钟内掉为 80，类似这种断崖式下跌是否是业务正常逻辑，可以对业务健康情况反向检测。</p>
<p><strong>发送耗时</strong></p>
<p>通过采集发送消息的耗时分布情况，了解客户端的发送情况，耗时分布可以为下面区间，单位毫秒。[0, 1), [1, 5), [5, 10), [10, 50), [50, 100), [100, 500), [500, 1000), [1000, ∞)。例如：如果发送的消息耗时分布集中在大于 500ms~1000ms，那需要介入分析原因为何耗时如此长。</p>
<p><strong>消息大小</strong></p>
<p>通过采集消息大小的分布情况，了解那些客户端存在大消息。发送速率过高的大消息同样存在集群的安全隐患。比如那些主题发送的消息大于 5K，为日后需要专项治理或者实时告警提供数据支撑。消息大小分布区间如下参考，单位 KB。[0, 1), [1, 5), [5, 10), [10, 50), [50, 100), [500, 1000), [1000, ∞)。</p>
<p><strong>日消息量</strong></p>
<p>日消息量是指通过每天采集的发送的消息数量，形成时间曲线。可以分析一周、一月的消息总量变化情况。</p>
<h4><strong>消费监控</strong></h4>
<p><strong>消费速度</strong></p>
<p>通过实时采集消费速度指标，掌握消费组健康情况。同样有些场景对消费速度大小比较关心。通过采集实时消息消费速率情况，为告警提供数据支撑。</p>
<p><strong>消费积压</strong></p>
<p>消费积压是指某一时刻还有多少消息没有消费，消费积压 = 发送消息总量 - 消费消息总量。消息积压是消费组监控指标中最重要的一项，有一些准实时场景对积压有着严苛的要求，那对消费积压指标的采集和告警就尤为重要。</p>
<p><strong>消费耗时</strong></p>
<p>消费耗时是从客户端采集的指标，通过采集客户端消费耗时分布情况检测客户端消费情况。通过消费耗时可以观察到客户端是否有阻塞情况、以及协助使用同学排查定位问题。</p>
<h3>监控开发实战</h3>
<p>在上面梳理的主题监控和消费监控的指标中，有些指标需要从 RocketMQ 集群采集，例如：发送速度、日消息量、消费速度、消费积压。有些指标需要客户端上报，例如：发送耗时、发送消息体大小、消费耗时。</p>
<p><img src="assets/20200830092314836.png" alt="img" /></p>
<h4><strong>实战部分说明</strong></h4>
<p>下面代码中用到的定时任务调度、getMqAdmin 等工具类见 《RocketMQ 集群监控（一）》，关于调度采集频率，可以选择 1 秒或者 5 秒均可。</p>
<p>上图中的“指标采集相关主题”，考虑到有的公司可能几千上万的应用，可以采用 Kafka 来做。</p>
<p>下面实战中主要关注 RocketMQ 相关指标如何收集，上报到 Kafka 的指标主题以及存储时序数据库代码没有给出，这部分逻辑一个是发送，一个插入数据库，并不复杂，自行完善即可。</p>
<p>实践中建议提供 SDK 来封装发送和消费，同时将监控指标的采集也封装进去，这样对用户来说是无感知的。</p>
<h4><strong>收集主题发送速度</strong></h4>
<p>先获取了集群中的主题列表，然后统计每个主题在每个 Master 中的速率。最后将统计的结果上报到统计主题或者直接写入时序数据库。</p>
<p>另外，统计时将 MQ 内置一些主题过滤掉无需统计。例如：重试队列（%RETRY%）、死信队列（%DLQ%）。</p>
<pre><code>public void collectTopicTps() throws Exception {
    DefaultMQAdminExt mqAdmin = getMqAdmin();
    Set&lt;String&gt; topicList = mqAdmin.fetchTopicsByCLuster(&quot;demo_mq&quot;).getTopicList();
    ClusterInfo clusterInfo = mqAdmin.examineBrokerClusterInfo();
    Map&lt;String/*主题名称*/, Double/*Tps*/&gt; topicTps = Maps.newHashMap();
    // 统计主题在每个 Master 上的速度
    for (Map.Entry&lt;String, BrokerData&gt; stringBrokerDataEntry : clusterInfo.getBrokerAddrTable().entrySet()) {
        BrokerData brokerData = stringBrokerDataEntry.getValue();
        // 获取 Master 节点
        String brokerAddr = brokerData.getBrokerAddrs().get(MixAll.MASTER_ID);
        for (String topic : topicList) {
            try {
                //注意此处将%DLQ%、%RETRY%等 MQ 内置主题过滤掉
                if(topic.contains(&quot;%DLQ%&quot;)|| topic.contains(&quot;%RETRY%&quot;)){
                    continue;
                }
                BrokerStatsData topicPutNums = mqAdmin.viewBrokerStatsData(brokerAddr, BrokerStatsManager.TOPIC_PUT_NUMS, topic);
                double topicTpsOnBroker = topicPutNums.getStatsMinute().getTps();
                if(topicTps.containsKey(topic)){
                    topicTps.put(topic, topicTps.get(topic) + topicTpsOnBroker);
                }else{
                    topicTps.put(topic,topicTpsOnBroker);
                }
            } catch (MQClientException ex) {
                ex.printStackTrace();
            }
        }
    }
    // 将采集到的主题速度，topicTps 上报到主题或者直接写入时序数据库即可
}

</code></pre>
<h4><strong>收集主题日消息量</strong></h4>
<p>日消息量的采集方式与主题发送速度的采集方式类似。由于是日消息量，采集频率可以一天执行一次。</p>
<pre><code>public void collectTopicMsgNums() throws Exception {
    DefaultMQAdminExt mqAdmin = getMqAdmin();
    Set&lt;String&gt; topicList = mqAdmin.fetchTopicsByCLuster(&quot;demo_mq&quot;).getTopicList();
    ClusterInfo clusterInfo = mqAdmin.examineBrokerClusterInfo();
    Map&lt;String/*主题名称*/, Long/*日消息量*/&gt; topicMsgNum = Maps.newHashMap();
    // 统计主题在每个 Master 上日消息量
    for (Map.Entry&lt;String, BrokerData&gt; stringBrokerDataEntry : clusterInfo.getBrokerAddrTable().entrySet()) {
        BrokerData brokerData = stringBrokerDataEntry.getValue();
        // 获取 Master 节点
        String brokerAddr = brokerData.getBrokerAddrs().get(MixAll.MASTER_ID);
        for (String topic : topicList) {
            try {
                //注意此处将%DLQ%、%RETRY%等 MQ 内置主题过滤掉
                if(topic.contains(&quot;%DLQ%&quot;)|| topic.contains(&quot;%RETRY%&quot;)){
                    continue;
                }
                BrokerStatsData topicPutNums = mqAdmin.viewBrokerStatsData(brokerAddr, BrokerStatsManager.TOPIC_PUT_NUMS, topic);
                long topicMsgNumOnBroker = topicPutNums.getStatsDay().getSum();
                if(topicMsgNum.containsKey(topic)){
                    topicMsgNum.put(topic, topicMsgNum.get(topic) + topicMsgNumOnBroker);
                }else{
                    topicMsgNum.put(topic,topicMsgNumOnBroker);
                }
            } catch (MQClientException ex) {
                // ex.printStackTrace();
            }
        }
    }
    // 将采集到的主题日消息量，topicMsgNum 上报到指标主题或者直接写入时序数据库即可
}

</code></pre>
<h4><strong>收集消费速度</strong></h4>
<p>下面代码循环集群中每个 Broker，汇总每个 Broker 中每个 messageQueue 的消费速度。代码 consumerTps 即包含了消费组与其对应的消费速度。</p>
<pre><code>public void collectConsumerTps() throws Exception {
    DefaultMQAdminExt mqAdmin = getMqAdmin();
    ClusterInfo clusterInfo = mqAdmin.examineBrokerClusterInfo();
    Map&lt;String/*消费者名称*/, Double/*消费 Tps*/&gt; consumerTps = Maps.newHashMap();
    // 统计主题在每个 Master 上的消费速率
    for (Map.Entry&lt;String, BrokerData&gt; stringBrokerDataEntry : clusterInfo.getBrokerAddrTable().entrySet()) {
        BrokerData brokerData = stringBrokerDataEntry.getValue();
        // 获取 Master 节点
        String brokerAddr = brokerData.getBrokerAddrs().get(MixAll.MASTER_ID);
        ConsumeStatsList consumeStatsList = mqAdmin.fetchConsumeStatsInBroker(brokerAddr, false, 5000);
        for (Map&lt;String, List&lt;ConsumeStats&gt;&gt; consumerStats : consumeStatsList.getConsumeStatsList()) {
            for (Map.Entry&lt;String, List&lt;ConsumeStats&gt;&gt; stringListEntry : consumerStats.entrySet()) {
                String consumer = stringListEntry.getKey();
                List&lt;ConsumeStats&gt; consumeStats = stringListEntry.getValue();
                Double tps = 0d;
                for (ConsumeStats consumeStat : consumeStats) {
                    tps += consumeStat.getConsumeTps();
                }
                if(consumerTps.containsKey(consumer)){
                    consumerTps.put(consumer, consumerTps.get(consumer) + tps);
                }else{
                    consumerTps.put(consumer,tps);
                }
            }
        }
    }
    // 将采集到的消费速率，consumerTps 上报到指标主题或者直接写入时序数据库即可
}

</code></pre>
<h4><strong>收集消费积压</strong></h4>
<p>消费组的积压统计，需要计算各个消费队列的积压，并将积压求和汇总。</p>
<pre><code>public void collectConsumerLag() throws Exception {
    DefaultMQAdminExt mqAdmin = getMqAdmin();
    ClusterInfo clusterInfo = mqAdmin.examineBrokerClusterInfo();
    Map&lt;String/*消费者名称*/, Long/*消费积压*/&gt; consumerLags = Maps.newHashMap();
    // 统计主题在每个 Master 上的消费积压
    for (Map.Entry&lt;String, BrokerData&gt; stringBrokerDataEntry : clusterInfo.getBrokerAddrTable().entrySet()) {
        BrokerData brokerData = stringBrokerDataEntry.getValue();
        // 获取 Master 节点
        String brokerAddr = brokerData.getBrokerAddrs().get(MixAll.MASTER_ID);
        ConsumeStatsList consumeStatsList = mqAdmin.fetchConsumeStatsInBroker(brokerAddr, false, 5000);
        for (Map&lt;String, List&lt;ConsumeStats&gt;&gt; consumerStats : consumeStatsList.getConsumeStatsList()) {
            for (Map.Entry&lt;String, List&lt;ConsumeStats&gt;&gt; stringListEntry : consumerStats.entrySet()) {
                String consumer = stringListEntry.getKey();
                List&lt;ConsumeStats&gt; consumeStats = stringListEntry.getValue();
                Long lag = 0L;
                for (ConsumeStats consumeStat : consumeStats) {
                    lag += computeTotalDiff(consumeStat.getOffsetTable());
                }
                if(consumerLags.containsKey(consumer)){
                    consumerLags.put(consumer, consumerLags.get(consumer) + lag);
                }else{
                    consumerLags.put(consumer,lag);
                }
            }
        }
    }
    // 将采集到的消费积压，consumerLags 上报到指标主题或者直接写入时序数据库即可
}

public long computeTotalDiff(HashMap&lt;MessageQueue, OffsetWrapper&gt; offsetTable) {
    long diffTotal = 0L;
    long diff = 0l;
    for(Iterator it = offsetTable.entrySet().iterator(); it.hasNext(); diffTotal += diff) {
        Map.Entry&lt;MessageQueue, OffsetWrapper&gt; next = (Map.Entry)it.next();
        long consumerOffset = next.getValue().getConsumerOffset();
        if(consumerOffset &gt; 0){
            diff = ((OffsetWrapper)next.getValue()).getBrokerOffset() - consumerOffset;
        }
    }
    return diffTotal;
}

</code></pre>
<h4><strong>收集发送耗时及消息大小</strong></h4>
<p>DistributionMetric 提供了两个方法，分别用于统计消息大小和发送耗时。耗时分布区间为：[0, 1), [1, 5), [5, 10), [10, 50), [50, 100), [100, 500), [500, 1000), [1000, ∞)，单位毫秒。消息大小分布区为：[0, 1), [1, 5), [5, 10), [10, 50), [50, 100), [500, 1000), [1000, ∞)，单位 KB。</p>
<pre><code>public class DistributionMetric {

    private String name;

    private LongAdder lessThan1Ms = new LongAdder();
    private LongAdder lessThan5Ms = new LongAdder();
    private LongAdder lessThan10Ms = new LongAdder();
    private LongAdder lessThan50Ms = new LongAdder();
    private LongAdder lessThan100Ms = new LongAdder();
    private LongAdder lessThan500Ms = new LongAdder();
    private LongAdder lessThan1000Ms = new LongAdder();
    private LongAdder moreThan1000Ms = new LongAdder();

    private LongAdder lessThan1KB = new LongAdder();
    private LongAdder lessThan5KB = new LongAdder();
    private LongAdder lessThan10KB = new LongAdder();
    private LongAdder lessThan50KB = new LongAdder();
    private LongAdder lessThan100KB = new LongAdder();
    private LongAdder lessThan500KB = new LongAdder();
    private LongAdder lessThan1000KB = new LongAdder();
    private LongAdder moreThan1000KB = new LongAdder();

    public static DistributionMetric newDistributionMetric(String name) {
        DistributionMetric distributionMetric = new DistributionMetric();
        distributionMetric.setName(name);
        return distributionMetric;

    }

    public void markTime(long costInMs) {
        if (costInMs &lt; 1) {
            lessThan1Ms.increment();
        } else if (costInMs &lt; 5) {
            lessThan5Ms.increment();
        } else if (costInMs &lt; 10) {
            lessThan10Ms.increment();
        } else if (costInMs &lt; 50) {
            lessThan50Ms.increment();
        } else if (costInMs &lt; 100) {
            lessThan100Ms.increment();
        } else if (costInMs &lt; 500) {
            lessThan500Ms.increment();
        } else if (costInMs &lt; 1000) {
            lessThan1000Ms.increment();
        } else {
            moreThan1000Ms.increment();
        }
    }

    public void markSize(long costInMs) {
        if (costInMs &lt; 1024) {
            lessThan1KB.increment();
        } else if (costInMs &lt; 5 * 1024) {
            lessThan5KB.increment();
        } else if (costInMs &lt; 10 * 1024) {
            lessThan10KB.increment();
        } else if (costInMs &lt; 50 * 1024) {
            lessThan50KB.increment();
        } else if (costInMs &lt; 100 * 1024) {
            lessThan100KB.increment();
        } else if (costInMs &lt; 500 * 1024) {
            lessThan500KB.increment();
        } else if (costInMs &lt; 1024 * 1024) {
            lessThan1000KB.increment();
        } else {
            moreThan1000KB.increment();
        }
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}

public class MetricInfo {

    private String name;

    private long lessThan1Ms;
    private long lessThan5Ms;
    private long lessThan10Ms;
    private long lessThan50Ms;
    private long lessThan100Ms;
    private long lessThan500Ms;
    private long lessThan1000Ms;
    private long moreThan1000Ms;

    private long lessThan1KB;
    private long lessThan5KB;
    private long lessThan10KB;
    private long lessThan50KB;
    private long lessThan100KB;
    private long lessThan500KB;
    private long lessThan1000KB;
    private long moreThan1000KB;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public long getLessThan1Ms() {
        return lessThan1Ms;
    }

    public void setLessThan1Ms(long lessThan1Ms) {
        this.lessThan1Ms = lessThan1Ms;
    }

    public long getLessThan5Ms() {
        return lessThan5Ms;
    }

    public void setLessThan5Ms(long lessThan5Ms) {
        this.lessThan5Ms = lessThan5Ms;
    }

    public long getLessThan10Ms() {
        return lessThan10Ms;
    }

    public void setLessThan10Ms(long lessThan10Ms) {
        this.lessThan10Ms = lessThan10Ms;
    }

    public long getLessThan50Ms() {
        return lessThan50Ms;
    }

    public void setLessThan50Ms(long lessThan50Ms) {
        this.lessThan50Ms = lessThan50Ms;
    }

    public long getLessThan100Ms() {
        return lessThan100Ms;
    }

    public void setLessThan100Ms(long lessThan100Ms) {
        this.lessThan100Ms = lessThan100Ms;
    }

    public long getLessThan500Ms() {
        return lessThan500Ms;
    }

    public void setLessThan500Ms(long lessThan500Ms) {
        this.lessThan500Ms = lessThan500Ms;
    }

    public long getLessThan1000Ms() {
        return lessThan1000Ms;
    }

    public void setLessThan1000Ms(long lessThan1000Ms) {
        this.lessThan1000Ms = lessThan1000Ms;
    }

    public long getMoreThan1000Ms() {
        return moreThan1000Ms;
    }

    public void setMoreThan1000Ms(long moreThan1000Ms) {
        this.moreThan1000Ms = moreThan1000Ms;
    }

    public long getLessThan1KB() {
        return lessThan1KB;
    }

    public void setLessThan1KB(long lessThan1KB) {
        this.lessThan1KB = lessThan1KB;
    }

    public long getLessThan5KB() {
        return lessThan5KB;
    }

    public void setLessThan5KB(long lessThan5KB) {
        this.lessThan5KB = lessThan5KB;
    }

    public long getLessThan10KB() {
        return lessThan10KB;
    }

    public void setLessThan10KB(long lessThan10KB) {
        this.lessThan10KB = lessThan10KB;
    }

    public long getLessThan50KB() {
        return lessThan50KB;
    }

    public void setLessThan50KB(long lessThan50KB) {
        this.lessThan50KB = lessThan50KB;
    }

    public long getLessThan100KB() {
        return lessThan100KB;
    }

    public void setLessThan100KB(long lessThan100KB) {
        this.lessThan100KB = lessThan100KB;
    }

    public long getLessThan500KB() {
        return lessThan500KB;
    }

    public void setLessThan500KB(long lessThan500KB) {
        this.lessThan500KB = lessThan500KB;
    }

    public long getLessThan1000KB() {
        return lessThan1000KB;
    }

    public void setLessThan1000KB(long lessThan1000KB) {
        this.lessThan1000KB = lessThan1000KB;
    }

    public long getMoreThan1000KB() {
        return moreThan1000KB;
    }

    public void setMoreThan1000KB(long moreThan1000KB) {
        this.moreThan1000KB = moreThan1000KB;
    }
}

</code></pre>
<p>ClientMetricCollect 类模拟发送时对消息发送的耗时与消息大小统计。通过定时任务调度 recordMetricInfo() 方法，将采集到数据上报到特定主题并存入时序数据库。即完成了发送耗时及消息大小的采集。</p>
<pre><code>public class ClientMetricCollect {

    public Map&lt;String, DefaultMQProducer&gt; producerMap = Maps.newHashMap();

    private DistributionMetric distributionMetric;

    public DefaultMQProducer getTopicProducer(String topic) throws MQClientException {

        if (!producerMap.containsKey(topic)){
            DefaultMQProducer producer = new DefaultMQProducer(&quot;ProducerGroup&quot;.concat(&quot;_&quot;).concat(topic));
            producer.setNamesrvAddr(&quot;dev-mq3.ttbike.com.cn:9876&quot;);
            producer.setVipChannelEnabled(false);
            producer.setClientIP(&quot;mq producer-client-id-1&quot;);
            try {
                producer.start();
                this.distributionMetric = DistributionMetric.newDistributionMetric(topic);
                producerMap.put(topic,producer);
            } catch (MQClientException e) {
                throw e;
            }

        }
        return producerMap.get(topic);
    }

    public void send( Message message) throws Exception {
        long begin = System.currentTimeMillis();
        SendResult sendResult = null;
        sendResult = getTopicProducer(message.getTopic()).send(message);
        SendStatus sendStatus = sendResult.getSendStatus();
        if (sendStatus.equals(SendStatus.SEND_OK)) {
            long duration = System.currentTimeMillis() - begin;
            distributionMetric.markTime(duration);
            distributionMetric.markSize(message.getBody().length);
        }
    }

    public void recordMetricInfo(){
        MetricInfo metricInfo = new MetricInfo();
        metricInfo.setName(distributionMetric.getName());

        metricInfo.setLessThan1Ms(distributionMetric.getLessThan1Ms().longValue());
        metricInfo.setLessThan5Ms(distributionMetric.getLessThan5Ms().longValue());
        metricInfo.setLessThan10Ms(distributionMetric.getLessThan10Ms().longValue());
        metricInfo.setLessThan50Ms(distributionMetric.getLessThan50Ms().longValue());
        metricInfo.setLessThan100Ms(distributionMetric.getLessThan100Ms().longValue());
        metricInfo.setLessThan500Ms(distributionMetric.getLessThan500Ms().longValue());
        metricInfo.setLessThan1000Ms(distributionMetric.getLessThan1000Ms().longValue());
        metricInfo.setMoreThan1000Ms(distributionMetric.getMoreThan1000Ms().longValue());

        metricInfo.setLessThan1KB(distributionMetric.getLessThan1KB().longValue());
        metricInfo.setLessThan5KB(distributionMetric.getLessThan5KB().longValue());
        metricInfo.setLessThan10KB(distributionMetric.getLessThan10KB().longValue());
        metricInfo.setLessThan50KB(distributionMetric.getLessThan50KB().longValue());
        metricInfo.setLessThan100KB(distributionMetric.getLessThan100KB().longValue());
        metricInfo.setLessThan500KB(distributionMetric.getLessThan500KB().longValue());
        metricInfo.setLessThan1000KB(distributionMetric.getLessThan1000KB().longValue());
        metricInfo.setMoreThan1000KB(distributionMetric.getMoreThan1000KB().longValue());

        // 将采集到的发送耗时与消息大小分布，metricInfo 上报到主题或者直接写入时序数据库即可
        // System.out.println(JSON.toJSONString(metricInfo));
    }

    @Test
    public void test() throws Exception {
        for(int i=0; i&lt;100; i++){
            byte[] TEST_MSG = &quot;helloworld&quot;.getBytes();
            Message message = new Message(&quot;melon_online_test&quot;, TEST_MSG);
            send(message);
        }
    }

}

</code></pre>
<h4><strong>上报消费耗时</strong></h4>
<p>接着使用上面的公共类 DistributionMetric 的 markTime 来记录耗时情况，可以度量业务处理消息的耗时分布。耗时分布区间为：[0, 1), [1, 5), [5, 10), [10, 50), [50, 100), [100, 500), [500, 1000), [1000, ∞)，单位毫秒。</p>
<pre><code>public class ConsumerMetric {

    private DistributionMetric distributionMetric;

    public static void main(String[] args) throws Exception {
        String consumerName = &quot;demo_consumer&quot;;
        ConsumerMetric consumerMetric = new ConsumerMetric();
        consumerMetric.startConsume(consumerName);
    }

    public void startConsume(String consumerName) throws Exception{
        this.distributionMetric = DistributionMetric.newDistributionMetric(consumerName);
        DefaultMQPushConsumer consumer = new DefaultMQPushConsumer(consumerName);
        consumer.setNamesrvAddr(&quot;dev-mq3.ttbike.com.cn:9876&quot;);
        consumer.subscribe(&quot;melon_online_test&quot;, &quot;*&quot;);
        consumer.setConsumeFromWhere(ConsumeFromWhere.CONSUME_FROM_FIRST_OFFSET);
        //wrong time format 2017_0422_221800
        consumer.setConsumeTimestamp(&quot;20181109221800&quot;);
        consumer.registerMessageListener(new MessageListenerConcurrently() {

            @Override
            public ConsumeConcurrentlyStatus consumeMessage(List&lt;MessageExt&gt; msgs, ConsumeConcurrentlyContext context) {

                long begin = System.currentTimeMillis();

                // 处理业务逻辑
                System.out.printf(&quot;%s Receive New Messages: %s %n&quot;, Thread.currentThread().getName(), msgs);

                // 统计业务逻辑的消费耗时情况
                distributionMetric.markTime(System.currentTimeMillis() - begin);

                return ConsumeConcurrentlyStatus.CONSUME_SUCCESS;
            }
        });
        consumer.start();
        System.out.printf(&quot;Consumer Started.%n&quot;);
    }

    public void recordMetricInfo(){
        MetricInfo metricInfo = new MetricInfo();
        metricInfo.setName(distributionMetric.getName());

        metricInfo.setLessThan1Ms(distributionMetric.getLessThan1Ms().longValue());
        metricInfo.setLessThan5Ms(distributionMetric.getLessThan5Ms().longValue());
        metricInfo.setLessThan10Ms(distributionMetric.getLessThan10Ms().longValue());
        metricInfo.setLessThan50Ms(distributionMetric.getLessThan50Ms().longValue());
        metricInfo.setLessThan100Ms(distributionMetric.getLessThan100Ms().longValue());
        metricInfo.setLessThan500Ms(distributionMetric.getLessThan500Ms().longValue());
        metricInfo.setLessThan1000Ms(distributionMetric.getLessThan1000Ms().longValue());
        metricInfo.setMoreThan1000Ms(distributionMetric.getMoreThan1000Ms().longValue());

        // 将采集到的发送耗时与消息大小分布，metricInfo 上报到主题或者直接写入时序数据库即可
        // System.out.println(JSON.toJSONString(metricInfo));
    }
}

</code></pre>
<h4>发送变化率计算</h4>
<p>发送变化率的计算依托时序数据库的函数，发送 Tps 变化率 =(最大值 - 最小值)/中位数。下图示例中，5 分钟的 TPS 变化率为 3%。可以定时调度计算该指标，超过阈值（例如：100%）可以发送告警信息。</p>
<pre><code>&gt; select SPREAD(value)/MEDIAN(value) from mq_topic_info where clusterName='demo_mq' and topicName='max_bonus_send_topic' and &quot;name&quot;='tps' and &quot;time&quot; &gt; now()-5m ;
name: mq_topic_info
time                spread_median
----                -------------
1598796048448226482 0.03338460146566541
</code></pre>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="19&#32;RocketMQ&#32;集群监控（一）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="21&#32;RocketMQ&#32;集群告警.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434b1d5e7970ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
