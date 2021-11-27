<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>19 RocketMQ 集群监控（一）.md</title>
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

                    <a class="current-tab" href="19&#32;RocketMQ&#32;集群监控（一）.md">19 RocketMQ 集群监控（一）.md</a>
                    

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
                        <div><h1>19 RocketMQ 集群监控（一）</h1>
<h3>前言</h3>
<p>在 RocketMQ 体系中，有集群、主题、消费组，集群又包括 NameSrv 和 Broker。本篇主要介绍 RocketMQ 的集群监控设计应该考虑哪些方面，以及如何实现。下一篇文章介绍主题、消费组方面的监控。本篇的介绍基于实战中 4 主 4 从，主从异步复制的架构模式。</p>
<h3>监控项设计</h3>
<p>集群监控的目的记录集群健康状态，具体监控项见下图：</p>
<p><img src="assets/20200822095602855.png" alt="img" /></p>
<h4><strong>节点数量</strong></h4>
<p>如果集群中是 4 主 4 从架构，那么集群中会有 8 个 Broker 节点，下面通过 clusterList 命令可以看到有 8 个节点。当集群中节点数量小于 8 时，说明集群中有节点掉线。</p>
<pre><code>$ bin/mqadmin clusterList -n x.x.x.x:9876
RocketMQLog:WARN No appenders could be found for logger (io.netty.util.internal.PlatformDependent0).
RocketMQLog:WARN Please initialize the logger system properly.
#Cluster Name  #Broker Name         #BID  #Addr                  #Version                #InTPS(LOAD)       #OutTPS(LOAD) #PCWait(ms) #Hour #SPACE
demo_mq        demo_mq_a            0     10.111.89.111:10911    V4_7_0                 380.96(0,0ms)       383.16(0,0ms)          0 557.15 0.2298
demo_mq        demo_mq_a            1     10.111.89.110:10915    V4_7_0                 380.76(0,0ms)         0.00(0,0ms)          0 557.15 0.4734
demo_mq        demo_mq_b            0     10.111.89.112:10911    V4_7_0                 391.86(0,0ms)       381.66(0,0ms)          0 557.22 0.2437
demo_mq        demo_mq_b            1     10.111.89.110:10925    V4_7_0                 391.26(0,0ms)         0.00(0,0ms)          0 557.22 0.4734
demo_mq        demo_mq_c            0     10.111.26.96:10911     V4_7_0                 348.37(0,0ms)       342.77(0,0ms)          0 557.22 0.2428
demo_mq        demo_mq_c            1     10.111.26.91:10925     V4_7_0                 357.66(0,0ms)         0.00(0,0ms)          0 557.22 0.4852
demo_mq        demo_mq_d            0     10.111.26.81:10911     V4_7_0                 421.16(0,0ms)       409.86(0,0ms)          0 557.18 0.2424
demo_mq        demo_mq_d            1     10.111.26.91:10915     V4_7_0                 423.30(0,0ms)         0.00(0,0ms)          0 557.18 0.4852

</code></pre>
<h4><strong>节点可用性</strong></h4>
<p>检测集群中节点的是否可用也很重要，Broker 节点数量或者进程的检测不能保证节点是否可用。这个容易理解，比如 Broker 进程在，但是可能不能提供正常服务或者假死状态。我们可以通过定时向集群中各个 Broker 节点发送心跳的方式来检测。另外，记录发送的响应时间也很关键，响应时间过长，例如超过 5 秒，往往伴随着集群抖动，具体体现为客户端发送超时。</p>
<p>可用性心跳检测：</p>
<ul>
<li>发送成功：表示该节点运行正常</li>
<li>发送失败：表示该节点运行异常</li>
</ul>
<p>响应时间检测：</p>
<ul>
<li>响应正常：响应时间在几毫秒到几十毫秒，是比较合理的范围</li>
<li>响应过长：响应时间大于 1 秒，甚至超过 5 秒，是不正常的，需要介入调查</li>
</ul>
<h4><strong>集群写入 TPS</strong></h4>
<p>在前面的文章中介绍了 RocketMQ 集群的性能摸高，文章中测试场景最高为 12 万多 TPS。那我们预计承载范围 4 万~6 万，留有一定的增长空间。持续监测集群写入的 TPS，使集群保持在我们预计的承载范围。从 clusterList 命令中，可以看到每个节点的 InTPS，将各个 Master 节点求和即为集群的 TPS。</p>
<h4><strong>集群写入 TPS 变化率</strong></h4>
<p>考虑到过高的瞬时流量会使集群发生流控，那么集群写入的 TPS 变化率监控就比较重要了。我们可以在集群写入 TPS 监控数据的基础上通过时序数据库函数统计集群 TPS 在某一段时间内的变化率。</p>
<h3>监控开发实战</h3>
<p>本小节中会给出监控设计的架构图示和示例代码，通过采集服务采集 RocketMQ 监控指标，并将其存储在时序数据库中，例如 InfluxDB。</p>
<p><img src="assets/20200822150652834.png" alt="img" /></p>
<h4><strong>准备工作</strong></h4>
<p>\1. 定时任务调度，以 10 秒钟为例：</p>
<pre><code>ScheduledExecutorService executorService = Executors.newScheduledThreadPool(1, new ThreadFactory() {
  @Override
  public Thread newThread(Runnable r) {
      return new Thread(r,  &quot;rocketMQ metrics collector&quot;);
  }
});
executorService.scheduleAtFixedRate(new Runnable() {
  @Override
  public void run() {
      // 指标收集方法 1 collectClusterNum()
      // 指标收集方法 2 collectMetric2()
  }
}, 60, 10, TimeUnit.SECONDS);

</code></pre>
<p>\2. 获取 Broker TPS 时用到了 MQAdmin，下面是初始化代码：</p>
<pre><code>public DefaultMQAdminExt getMqAdmin() throws MQClientException {
  DefaultMQAdminExt defaultMQAdminExt = new DefaultMQAdminExt();
  defaultMQAdminExt.setNamesrvAddr(&quot;x.x.x.x:9876&quot;);
  defaultMQAdminExt.setInstanceName(Long.toString(System.currentTimeMillis()));
  defaultMQAdminExt.setVipChannelEnabled(false);
  defaultMQAdminExt.start();
  return defaultMQAdminExt;
}

</code></pre>
<p>\3. 发送 Producer 启动代码：</p>
<pre><code>public DefaultMQProducer getMqProducer(){
    DefaultMQProducer producer = new DefaultMQProducer(&quot;rt_collect_producer&quot;);
    producer.setNamesrvAddr(&quot;&quot;);
    producer.setVipChannelEnabled(false);
    producer.setClientIP(&quot;mq producer-client-id-1&quot;);
    try {
        producer.start();
    } catch (MQClientException e) {
        e.getErrorMessage();
    }
    return producer;
}

</code></pre>
<h4><strong>收集集群节点数量</strong></h4>
<p>下面代码中统计了集群中的主节点和从节点总数量，定时调用该收集方法，并将其记录在时序数据中。</p>
<pre><code>public void collectClusterNum() throws Exception {
  DefaultMQAdminExt mqAdmin = getMqAdmin();
  ClusterInfo clusterInfo = mqAdmin.examineBrokerClusterInfo();
  int brokers = 0;
  Set&lt;Map.Entry&lt;String, BrokerData&gt;&gt; entries = clusterInfo.getBrokerAddrTable().entrySet();
  for (Map.Entry&lt;String, BrokerData&gt; entry : entries) {
  brokers += entry.getValue().getBrokerAddrs().entrySet().size();
  }
  // 将 brokers 存储到时序数据库即可
  System.out.println(brokers);
}

</code></pre>
<h4><strong>收集节点可用性</strong></h4>
<p>集群中的每个 Broker 的可用性，可以通过定时发送信息到该 Broker 特定的主题来实现。例如：集群中有 broker-a、broker-b、broker-c、broker-d。那每个 broker-a 上有一个名字为“broker-a”的主题，其他节点同理。通过定时向该主题发送心跳来实现可用性。</p>
<p>下面两个 ClusterRtTime 和 RtTime 分别为集群和 Broker 的收集的数据填充类。</p>
<pre><code>public class ClusterRtTime {
    private String cluster;

    private List&lt;RtTime&gt; times;

    private long timestamp = System.currentTimeMillis();

    public long getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(long timestamp) {
        this.timestamp = timestamp;
    }

    public String getCluster() {
        return cluster;
    }

    public void setCluster(String cluster) {
        this.cluster = cluster;
    }

    public List&lt;RtTime&gt; getTimes() {
        return times;
    }

    public void setTimes(List&lt;RtTime&gt; times) {
        this.times = times;
    }
}

public class RtTime {
    private long rt;

    private String brokerName;

    private String status;

    private int result;

    public int getResult() {
        return result;
    }

    public void setResult(int result) {
        this.result = result;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public long getRt() {
        return rt;
    }
    public void setRt(long rt) {
        this.rt = rt;
    }
    public String getBrokerName() {
        return brokerName;
    }
    public void setBrokerName(String brokerName) {
        this.brokerName = brokerName;
    }
}

</code></pre>
<p>以下方法为同步发送心跳检测实现，以 broker-a 为例，time.setRt 表示每次发送心跳的耗时，time.setResult 表示每次发送心跳的结果，成功还是失败。</p>
<pre><code> public void collectRtTime() throws Exception {
   DefaultMQAdminExt mqAdmin = getMqAdmin();
   ClusterRtTime clusterRtTime = new ClusterRtTime();
   ClusterInfo clusterInfo = null;
   try {
   clusterInfo = mqAdmin.examineBrokerClusterInfo();
   } catch (Exception e) {
   e.printStackTrace();
   return;
   }
   clusterRtTime.setCluster(&quot;demo_mq&quot;);
   List&lt;RtTime&gt; times = Lists.newArrayList();
   for (Map.Entry&lt;String, BrokerData&gt; stringBrokerDataEntry : clusterInfo.getBrokerAddrTable().entrySet()) {
   BrokerData brokerData = stringBrokerDataEntry.getValue();
   String brokerName = brokerData.getBrokerName();
   long begin = System.currentTimeMillis();
   SendResult sendResult = null;
   RtTime time = new RtTime();
   time.setBrokerName(brokerName);
   try {
   byte[] TEST_MSG = &quot;helloworld&quot;.getBytes();
   sendResult = getMqProducer().send(new Message(brokerName, TEST_MSG));
   long end = System.currentTimeMillis() - begin;
   SendStatus sendStatus = sendResult.getSendStatus();
   // 记录发送耗时情况
   time.setRt(end);
   // 记录发送是否成功情况
   time.setStatus(sendStatus.name());
   time.setResult(sendStatus.ordinal());
   } catch (Exception e) {
   time.setRt(-1);
   time.setStatus(&quot;FAILED&quot;);
   time.setResult(5);
   }
   times.add(time);
   }
   clusterRtTime.setTimes(times);
   // 将 clusterRtTime 信息存储到时序数据库即可
 }

</code></pre>
<h4><strong>收集集群 TPS</strong></h4>
<p>结合定时任务调度下面的收集集群 TPS 方法，将其存储到时序数据库中。如果 10 秒收集一次，那么 1 分钟可以收集 6 次集群 TPS。</p>
<pre><code> public void collectClusterTps() throws Exception {
 DefaultMQAdminExt mqAdmin = getMqAdmin();
 ClusterInfo clusterInfo = mqAdmin.examineBrokerClusterInfo();
 double totalTps = 0d;
 for (Map.Entry&lt;String, BrokerData&gt; stringBrokerDataEntry : clusterInfo.getBrokerAddrTable().entrySet()) {
            BrokerData brokerData = stringBrokerDataEntry.getValue();
            // 选择 Master 节点
            String brokerAddr = brokerData.getBrokerAddrs().get(MixAll.MASTER_ID);
            if (StringUtils.isBlank(brokerAddr)) continue;
            KVTable runtimeStatsTable = mqAdmin.fetchBrokerRuntimeStats(brokerAddr);
            HashMap&lt;String, String&gt; runtimeStatus = runtimeStatsTable.getTable();
            Double putTps = Math.ceil(Double.valueOf(runtimeStatus.get(&quot;putTps&quot;).split(&quot; &quot;)[0]));
            totalTps = totalTps + putTps;
  }
  // 将 totalTps 存储到时序数据库即可
  System.out.println(totalTps);
}

</code></pre>
<h4><strong>计算集群 TPS 的变化率</strong></h4>
<p>集群 TPS 的变化情况，我们可以通过时序数据库函数来实现。假设我们上面采集到的集群 TPS 写入到 InfluxDB 的 cluster_number_info 表中。下面语句表示 5 分钟内集群 Tps 的变化率。示例中 5 分钟内集群 TPS 变化了 12%，如果变化超过 50%，甚至 200%、300%，是需要我们去关注的，以免瞬时流量过高使集群发生流控，对业务造成超时影响。</p>
<p>写入 TPS 的变化率 = (最大值 - 最小值)/中位数</p>
<pre><code>&gt; select SPREAD(value)/MEDIAN(value) from cluster_number_info where clusterName='demo_mq' and &quot;name&quot;='totalTps' and &quot;time&quot; &gt; now()-5m ;
name: cluster_number_info
time                spread_median
----                -------------
1572941783075915928 0.12213740458015267
</code></pre>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="18&#32;RocketMQ&#32;集群平滑运维.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="20&#32;RocketMQ&#32;集群监控（二）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434b190bb870ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
