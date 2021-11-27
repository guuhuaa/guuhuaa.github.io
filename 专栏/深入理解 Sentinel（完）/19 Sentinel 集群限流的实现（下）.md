<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>19 Sentinel 集群限流的实现（下）.md</title>
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

                    
                    <a href="01&#32;开篇词：一次服务雪崩问题排查经历.md">01 开篇词：一次服务雪崩问题排查经历.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;为什么需要服务降级以及常见的几种降级方式.md">02 为什么需要服务降级以及常见的几种降级方式.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;为什么选择&#32;Sentinel，Sentinel&#32;与&#32;Hystrix&#32;的对比.md">03 为什么选择 Sentinel，Sentinel 与 Hystrix 的对比.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;Sentinel&#32;基于滑动窗口的实时指标数据统计.md">04 Sentinel 基于滑动窗口的实时指标数据统计.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;Sentinel&#32;的一些概念与核心类介绍.md">05 Sentinel 的一些概念与核心类介绍.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;Sentinel&#32;中的责任链模式与&#32;Sentinel&#32;的整体工作流程.md">06 Sentinel 中的责任链模式与 Sentinel 的整体工作流程.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;Java&#32;SPI&#32;及&#32;SPI&#32;在&#32;Sentinel&#32;中的应用.md">07 Java SPI 及 SPI 在 Sentinel 中的应用.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;资源指标数据统计的实现全解析（上）.md">08 资源指标数据统计的实现全解析（上）.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;资源指标数据统计的实现全解析（下）.md">09 资源指标数据统计的实现全解析（下）.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;限流降级与流量效果控制器（上）.md">10 限流降级与流量效果控制器（上）.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;限流降级与流量效果控制器（中）.md">11 限流降级与流量效果控制器（中）.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;限流降级与流量效果控制器（下）.md">12 限流降级与流量效果控制器（下）.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;熔断降级与系统自适应限流.md">13 熔断降级与系统自适应限流.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;黑白名单限流与热点参数限流.md">14 黑白名单限流与热点参数限流.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;自定义&#32;ProcessorSlot&#32;实现开关降级.md">15 自定义 ProcessorSlot 实现开关降级.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;Sentinel&#32;动态数据源：规则动态配置.md">16 Sentinel 动态数据源：规则动态配置.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;Sentinel&#32;主流框架适配.md">17 Sentinel 主流框架适配.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;Sentinel&#32;集群限流的实现（上）.md">18 Sentinel 集群限流的实现（上）.md</a>

                </li>
                <li>

                    <a class="current-tab" href="19&#32;Sentinel&#32;集群限流的实现（下）.md">19 Sentinel 集群限流的实现（下）.md</a>
                    

                </li>
                <li>

                    
                    <a href="20&#32;结束语：Sentinel&#32;对应用的性能影响如何？.md">20 结束语：Sentinel 对应用的性能影响如何？.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;番外篇：Sentinel&#32;1.8.0&#32;熔断降级新特性解读.md">21 番外篇：Sentinel 1.8.0 熔断降级新特性解读.md</a>

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
                        <div><h1>19 Sentinel 集群限流的实现（下）</h1>
<h3>集群限流源码分析</h3>
<p>集群限流，我们可以结合令牌桶算法去思考，服务端负责生产令牌，客户端向服务端申请令牌，客户端只有申请到令牌时才能将请求放行，否则拒绝请求。</p>
<p>集群限流也支持热点参数限流，而实现原理大致相同，所以关于热点参数的集群限流将留给大家自己去研究。</p>
<h4><strong>核心类介绍</strong></h4>
<p>sentinel-core 模块的 cluster 包下定义了实现集群限流功能的相关接口：</p>
<ul>
<li>TokenService：定义客户端向服务端申请 token 的接口，由 FlowRuleChecker 调用。</li>
<li>ClusterTokenClient：集群限流客户端需要实现的接口，继承 TokenService。</li>
<li>ClusterTokenServer：集群限流服务端需要实现的接口。</li>
<li>EmbeddedClusterTokenServer：支持嵌入模式的集群限流服务端需要实现的接口，继承 TokenService、ClusterTokenServer。</li>
</ul>
<p>TokenService 接口的定义如下：</p>
<pre><code class="language-java">public interface TokenService {
    TokenResult requestToken(Long ruleId, int acquireCount, boolean prioritized);
    TokenResult requestParamToken(Long ruleId, int acquireCount, Collection&lt;Object&gt; params);
}

</code></pre>
<ul>
<li>requestToken：向 server 申请令牌，参数 1 为集群限流规则 ID，参数 2 为申请的令牌数，参数 3 为请求优先级。</li>
<li>requestParamToken：用于支持热点参数集群限流，向 server 申请令牌，参数 1 为集群限流规则 ID，参数 2 为申请的令牌数，参数 3 为限流参数。</li>
</ul>
<p>TokenResult 实体类的定义如下：</p>
<pre><code class="language-java">public class TokenResult {
    private Integer status;
    private int remaining;
    private int waitInMs;
    private Map&lt;String, String&gt; attachments;
}

</code></pre>
<ul>
<li>status：请求的响应状态码。</li>
<li>remaining：当前时间窗口剩余的令牌数。</li>
<li>waitInMs：休眠等待时间，单位毫秒，用于告诉客户端，当前请求可以放行，但需要先休眠指定时间后才能放行。</li>
<li>attachments：附带的属性，暂未使用。</li>
</ul>
<p>ClusterTokenClient 接口定义如下：</p>
<pre><code class="language-java">public interface ClusterTokenClient extends TokenService {
    void start() throws Exception;
    void stop() throws Exception;
}

</code></pre>
<p>ClusterTokenClient 接口定义启动和停止集群限流客户端的方法，负责维护客户端与服务端的连接。该接口还继承了 TokenService，要求实现类必须要实现 requestToken、requestParamToken 方法，向远程服务端请求获取令牌。</p>
<p>ClusterTokenServer 接口定义如下：</p>
<pre><code class="language-java">public interface ClusterTokenServer {
    void start() throws Exception;
    void stop() throws Exception;
}

</code></pre>
<p>ClusterTokenServer 接口定义启动和停止集群限流客户端的方法，启动能够接收和响应客户端请求的网络通信服务端，根据接收的消费类型处理客户端的请求。</p>
<p>EmbeddedClusterTokenServer 接口的定义如下：</p>
<pre><code class="language-java">public interface EmbeddedClusterTokenServer 
                 extends ClusterTokenServer, TokenService {
}

</code></pre>
<p>EmbeddedClusterTokenServer 接口继承 ClusterTokenServer，并继承 TokenService 接口，即整合客户端和服务端的功能，为嵌入式模式提供支持。在嵌入式模式下，如果当前节点是集群限流服务端，那就没有必要发起网络请求。</p>
<p>这些接口以及默认实现类的关系如下图所示。</p>
<p><img src="assets/a3a9f1c0-f5b9-11ea-a625-2d171281165b" alt="19-01-classs" /></p>
<p>其中 DefaultClusterTokenClient 是 sentinel-cluster-client-default 模块中的 ClusterTokenClient 接口实现类，DefaultTokenService 与 DefaultEmbeddedTokenServer 分别是 sentinel-cluster-server-default 模块中的 ClusterTokenServer 接口与 EmbeddedClusterTokenServer 接口的实现类。</p>
<p>当使用嵌入模式启用集群限流服务端时，使用的是 EmbeddedClusterTokenServer，否则使用 ClusterTokenServer，通过 Java SPI 实现。</p>
<h4><strong>集群限流客户端</strong></h4>
<p>我们接着单机限流工作流程分析集群限流功能的实现，从 FlowRuleChecker#passClusterCheck 方法开始，该方法源码如下。</p>
<pre><code class="language-java">private static boolean passClusterCheck(FlowRule rule, Context context, DefaultNode node, int acquireCount,boolean prioritized) {
        try {
            // (1)
            TokenService clusterService = pickClusterService();
            if (clusterService == null) {
                return fallbackToLocalOrPass(rule, context, node, acquireCount, prioritized);
            }
            // (2)
            long flowId = rule.getClusterConfig().getFlowId();
            // (3)
            TokenResult result = clusterService.requestToken(flowId, acquireCount, prioritized);
            return applyTokenResult(result, rule, context, node, acquireCount, prioritized);
        } catch (Throwable ex) {
            RecordLog.warn(&quot;[FlowRuleChecker] Request cluster token unexpected failed&quot;, ex);
        }
         // (4)
        return fallbackToLocalOrPass(rule, context, node, acquireCount, prioritized);
    }

</code></pre>
<p>整体流程分为：</p>
<ol>
<li>获取 TokenService；</li>
<li>获取集群限流规则的全局唯一 ID；</li>
<li>调用 TokenService#requestToken 方法申请令牌；</li>
<li>调用 applyTokenResult 方法，根据请求响应结果判断是否需要拒绝当前请求。</li>
</ol>
<p>pickClusterService 方法实现根据节点当前角色获取 TokenService 实例。如果当前节点是集群限流客户端角色，则获取 ClusterTokenClient 实例，如果当前节点是集群限流服务端角色（嵌入模式），则获取 EmbeddedClusterTokenServer 实例，代码如下。</p>
<pre><code class="language-java">private static TokenService pickClusterService() {
    // 客户端角色
    if (ClusterStateManager.isClient()) {
        return TokenClientProvider.getClient();
    }
    // 服务端角色（嵌入模式）
    if (ClusterStateManager.isServer()) {
        return EmbeddedClusterTokenServerProvider.getServer();
    }
    return null;
}

</code></pre>
<p>ClusterTokenClient 和 EmbeddedClusterTokenServer 都继承 TokenService，区别在于，ClusterTokenClient 实现类实现 requestToken 方法是向服务端发起请求，而 EmbeddedClusterTokenServer 实现类实现 requestToken 方法不需要发起远程调用，因为自身就是服务端。</p>
<p>在拿到 TokenService 后，调用 TokenService#requestToken 方法请求获取 token。如果当前节点角色是集群限流客户端，那么这一步骤就是将方法参数构造为请求数据包，向集群限流服务端发起请求，并同步等待获取服务端的响应结果。关于网络通信这块，因为不是专栏的重点，所以我们不展开分析。</p>
<p>applyTokenResult 方法源码如下：</p>
<pre><code class="language-java">private static boolean applyTokenResult(/*@NonNull*/ TokenResult result, FlowRule rule, Context context,
                                                         DefaultNode node,
                                                         int acquireCount, boolean prioritized) {
        switch (result.getStatus()) {
            case TokenResultStatus.OK:
                return true;
            case TokenResultStatus.SHOULD_WAIT:
                try {
                    Thread.sleep(result.getWaitInMs());
                } catch (InterruptedException e) {
                }
                return true;
            case TokenResultStatus.NO_RULE_EXISTS:
            case TokenResultStatus.BAD_REQUEST:
            case TokenResultStatus.FAIL:
            case TokenResultStatus.TOO_MANY_REQUEST:
                return fallbackToLocalOrPass(rule, context, node, acquireCount, prioritized);
            case TokenResultStatus.BLOCKED:
            default:
                return false;
        }
    }

</code></pre>
<p>applyTokenResult 方法根据响应状态码决定是否拒绝当前请求：</p>
<ul>
<li>当响应状态码为 OK 时放行请求；</li>
<li>当响应状态码为 SHOULD_WAIT 时，休眠指定时间再放行请求；</li>
<li>当响应状态码为 BLOCKED，直接拒绝请求；</li>
<li>其它状态码均代表调用失败，根据规则配置的 fallbackToLocalWhenFail 是否为 true，决定是否回退为本地限流，如果需要回退为本地限流模式，则调用 passLocalCheck 方法重新判断。</li>
</ul>
<p>在请求异常或者服务端响应异常的情况下，都会走 fallbackToLocalOrPass 方法，该方法源码如下。</p>
<pre><code class="language-java">private static boolean fallbackToLocalOrPass(FlowRule rule, Context context, DefaultNode node, int acquireCount, boolean prioritized) {
        if (rule.getClusterConfig().isFallbackToLocalWhenFail()) {
            return passLocalCheck(rule, context, node, acquireCount, prioritized);
        } else {
            // The rule won't be activated, just pass.
            return true;
        }
}

</code></pre>
<p>fallbackToLocalOrPass 方法根据规则配置的 fallbackToLocalWhenFail 决定是否回退为本地限流，如果 fallbackToLocalWhenFail 配置为 false，将会导致客户端在与服务端失联的情况下拒绝所有流量。fallbackToLocalWhenFail 默认值为 true，建议不要修改为 false，我们应当确保服务的可用性，再确保集群限流的准确性。</p>
<p>由于网络延迟的存在，Sentinel 集群限流并未实现匀速排队流量效果控制，也没有支持冷启动，而只支持直接拒绝请求的流控效果。响应状态码 SHOULD_WAIT 并非用于实现匀速限流，而是用于实现具有优先级的请求在达到限流阈值的情况下，可试着占据下一个时间窗口的 pass 指标，如果抢占成功，则告诉限流客户端，当前请求需要休眠等待下个时间窗口的到来才可以通过。Sentinel 使用提前申请在未来时间通过的方式实现优先级语意。</p>
<h4><strong>集群限流服务端</strong></h4>
<p>在集群限流服务端接收到客户端发来的 requestToken 请求时，或者嵌入模式自己向自己发起请求，最终都会交给 DefaultTokenService 处理。DefaultTokenService 实现的 requestToken 方法源码如下。</p>
<pre><code class="language-java">    @Override
    public TokenResult requestToken(Long ruleId, int acquireCount, boolean prioritized) {
        // 验证规则是否存在
        if (notValidRequest(ruleId, acquireCount)) {
            return badRequest();
        }
        // （1）
        FlowRule rule = ClusterFlowRuleManager.getFlowRuleById(ruleId);
        if (rule == null) {
            return new TokenResult(TokenResultStatus.NO_RULE_EXISTS);
        }
        // （2）
        return ClusterFlowChecker.acquireClusterToken(rule, acquireCount, prioritized);
    }

</code></pre>
<ul>
<li>根据限流规则 ID 获取到限流规则，这也是要求集群限流规则的 ID 全局唯一的原因，Sentinel 只使用一个 ID 字段向服务端传递限流规则，减小了数据包的大小，从而优化网络通信的性能；</li>
<li>调用 ClusterFlowChecker#acquireClusterToken 方法判断是否拒绝请求。</li>
</ul>
<p>由于 ClusterFlowChecker#acquireClusterToken 方法源码太多，我们将 acquireClusterToken 拆分为四个部分分析。</p>
<p>第一个部分代码如下：</p>
<pre><code class="language-java">static TokenResult acquireClusterToken(FlowRule rule, int acquireCount, boolean prioritized) {
        Long id = rule.getClusterConfig().getFlowId();
        // （1）
        if (!allowProceed(id)) {
            return new TokenResult(TokenResultStatus.TOO_MANY_REQUEST);
        }
        // （2）
        ClusterMetric metric = ClusterMetricStatistics.getMetric(id);
        if (metric == null) {
            return new TokenResult(TokenResultStatus.FAIL);
        }
        // （3）
        double latestQps = metric.getAvg(ClusterFlowEvent.PASS);
        double globalThreshold = calcGlobalThreshold(rule) * ClusterServerConfigManager.getExceedCount();
        double nextRemaining = globalThreshold - latestQps - acquireCount;
        if (nextRemaining &gt;= 0) {
            // 第二部分代码
        } else {
            if (prioritized) {
                // 第三部分代码
            }
            // 第四部分代码
        }
    }

</code></pre>
<p>全局 QPS 阈值限流，按名称空间统计 QPS，如果需要使用按名称空间 QPS 限流，则可通过如下方式配置阈值。</p>
<pre><code class="language-java">  ServerFlowConfig serverFlowConfig = new ServerFlowConfig();
  serverFlowConfig.setMaxAllowedQps(1000);
  ClusterServerConfigManager.loadFlowConfig(&quot;serviceA&quot;,serverFlowConfig);

</code></pre>
<ul>
<li>获取规则的指标数据统计滑动窗口，如果不存在则响应 FAIL 状态码；</li>
<li>计算每秒平均被放行请求数、集群限流阈值、剩余可用令牌数量。</li>
</ul>
<p>计算集群限流阈值需根据规则配置的阈值类型计算，calcGlobalThreshold 方法的源码如下。</p>
<pre><code class="language-java">private static double calcGlobalThreshold(FlowRule rule) {
        double count = rule.getCount();
        switch (rule.getClusterConfig().getThresholdType()) {
            case ClusterRuleConstant.FLOW_THRESHOLD_GLOBAL:
                return count;
            case ClusterRuleConstant.FLOW_THRESHOLD_AVG_LOCAL:
            default:
                int connectedCount = ClusterFlowRuleManager.getConnectedCount(rule.getClusterConfig().getFlowId());
                return count * connectedCount;
        }
}

</code></pre>
<ul>
<li>当阈值类型为集群总 QPS 时，直接使用限流规则的阈值（count）；</li>
<li>当阈值类型为单机均摊时，根据规则 ID 获取当前连接的客户端总数，将当前连接的客户端总数乘以限流规则的阈值（count）作为集群总 QPS 阈值。</li>
</ul>
<p>这正是客户端在连接上服务端时，发送 PING 类型消费给服务端，并将名称空间携带在 PING 数据包上传递给服务端的原因。在限流规则的阈值为单机均摊阈值类型时，需要知道哪些连接是与限流规则所属名称空间相同，如果客户端不传递名称空间给服务端，那么，在单机均摊阈值类型情况下，计算出来的集群总 QPS 限流阈值将为 0，导致所有请求都会被限流。这是我们在使用集群限流功能时特别需要注意的。</p>
<p>集群限流阈值根据规则配置的阈值、阈值类型计算得到，每秒平均被放行请求数可从滑动窗口取得，而剩余可用令牌数（nextRemaining）等于集群 QPS 阈值减去当前时间窗口已经放行的请求数，再减去当前请求预占用的 acquireCount。</p>
<p>第二部分代码如下 ：</p>
<pre><code class="language-java">metric.add(ClusterFlowEvent.PASS, acquireCount);
metric.add(ClusterFlowEvent.PASS_REQUEST, 1);
if (prioritized) {
      metric.add(ClusterFlowEvent.OCCUPIED_PASS, acquireCount);
}
return new TokenResult(TokenResultStatus.OK).setRemaining((int) nextRemaining).setWaitInMs(0);

</code></pre>
<p>当 nextRemaining 计算结果大于等于 0 时，执行这部分代码，先记录当前请求被放行，而后响应状态码 OK 给客户端。</p>
<p>第三部分代码如下：</p>
<pre><code class="language-java">double occupyAvg = metric.getAvg(ClusterFlowEvent.WAITING);
if (occupyAvg &lt;= ClusterServerConfigManager.getMaxOccupyRatio() * globalThreshold) {
    int waitInMs = metric.tryOccupyNext(ClusterFlowEvent.PASS, acquireCount, globalThreshold);
    if (waitInMs &gt; 0) {
         return new TokenResult(TokenResultStatus.SHOULD_WAIT)
                  .setRemaining(0).setWaitInMs(waitInMs);
    }
}

</code></pre>
<p>当 nextRemaining 计算结果小于 0 时，如果当前请求具有优先级，则执行这部分逻辑。计算是否可占用下个时间窗口的 pass 指标，如果允许，则告诉客户端，当前请求可放行，但需要等待 waitInMs（一个窗口时间大小）毫秒之后才可放行。</p>
<p>如果请求可占用下一个时间窗口的 pass 指标，那么下一个时间窗口的 pass 指标也需要加上这些提前占用的请求总数，将会影响下一个时间窗口可通过的请求总数。</p>
<p>第四部分代码如下：</p>
<pre><code class="language-java">metric.add(ClusterFlowEvent.BLOCK, acquireCount);
metric.add(ClusterFlowEvent.BLOCK_REQUEST, 1);
if (prioritized) {
     metric.add(ClusterFlowEvent.OCCUPIED_BLOCK, acquireCount);
}
return blockedResult();

</code></pre>
<p>当 nextRemaining 大于 0，且无优先级权限时，直接拒绝请求，记录当前请求被 Block。</p>
<h3>集群限流的指标数据统计</h3>
<p>集群限流使用的滑动窗口并非 sentinel-core 模块下实现的滑动窗口，而是 sentinel-cluster-server-default 模块自己实现的滑动窗口。</p>
<p>ClusterFlowConfig 的 sampleCount 与 windowIntervalMs 这两个配置项正是用于为集群限流规则创建统计指标数据的滑动窗口，在加载集群限流规则时创建。如下源码所示。</p>
<pre><code class="language-java"> private static void applyClusterFlowRule(List&lt;FlowRule&gt; list, /*@Valid*/ String namespace) {
         ......
        for (FlowRule rule : list) {
            if (!rule.isClusterMode()) {
                continue;
            }
            ........
            ClusterFlowConfig clusterConfig = rule.getClusterConfig();
            .......
            // 如果不存在，则为规则创建 ClusterMetric，用于统计指标数据
            ClusterMetricStatistics.putMetricIfAbsent(flowId,
                new ClusterMetric(clusterConfig.getSampleCount(), 
                                  clusterConfig.getWindowIntervalMs()));
        }
        // 移除不再使用的 ClusterMetric
        clearAndResetRulesConditional(namespace, new Predicate&lt;Long&gt;() {
            @Override
            public boolean test(Long flowId) {
                return !ruleMap.containsKey(flowId);
            }
        });
        FLOW_RULES.putAll(ruleMap);
        NAMESPACE_FLOW_ID_MAP.put(namespace, flowIdSet);
    }

</code></pre>
<p>实现集群限流需要收集的指标数据有以下几种：</p>
<pre><code class="language-java">public enum ClusterFlowEvent {
    PASS,
    BLOCK,
    PASS_REQUEST,
    BLOCK_REQUEST,
    OCCUPIED_PASS,
    OCCUPIED_BLOCK,
    WAITING
}

</code></pre>
<ul>
<li>PASS：已经发放的令牌总数</li>
<li>BLOCK：令牌申请被驳回的总数</li>
<li>PASS_REQUEST：被放行的请求总数</li>
<li>BLOCK_REQUEST：被拒绝的请求总数</li>
<li>OCCUPIED_PASS：预占用，已经发放的令牌总数</li>
<li>OCCUPIED_BLOCK：预占用，令牌申请被驳回的总数</li>
<li>WAITING：当前等待下一个时间窗口到来的请求总数</li>
</ul>
<p>除统计的指标项与 sentinel-core 包下实现的滑动窗口统计的指标项有些区别外，实现方式都一致。</p>
<h3>集群限流总结</h3>
<p>集群限流服务端允许嵌入应用服务启动，也可作为独立应用启动。嵌入模式适用于单个微服务应用的集群内部实现集群限流，独立模式适用于多个微服务应用共享同一个集群限流服务端场景，独立模式不会影响应用性能，而嵌入模式对应用性能会有所影响。</p>
<p>集群限流客户端需指定名称空间，默认会使用 main 方法所在类的全类名作为名称空间。在客户端连接到服务端时，客户端会立即向服务端发送一条 PING 消息，并在 PING 消息携带名称空间给服务端。</p>
<p>集群限流规则的阈值类型支持单机均摊和集群总 QPS 两种类型，如果是单机均摊阈值类型，集群限流服务端需根据限流规则的名称空间，获取该名称空间当前所有的客户端连接，将连接总数乘以规则配置的阈值作为集群的总 QPS 阈值。</p>
<p>集群限流支持按名称空间全局限流，无视规则，只要是同一名称空间的客户端发来的 requestToken 请求，都先按名称空间阈值过滤。但并没有特别实用的场景，因此官方文档也并未介绍此特性。</p>
<p>建议按应用区分名称空间，而不是整个项目的所有微服务项目都使用同一个名称空间，因为在规则阈值类型为单机均摊阈值类型的情况下，获取与规则所属名称空间相同的客户端连接数作为客户端总数，如果不是同一个应用，就会导致获取到的客户端总数是整个项目所有微服务应用集群的客户端总数，限流就会出问题。</p>
<p>集群限流并非解决请求倾斜问题，在请求倾斜严重的情况下，集群限流可能会导致某些节点的流量过高，导致系统的负载过高，这时就需要使用系统自适应限流、熔断降级作为兜底解决方案。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="18&#32;Sentinel&#32;集群限流的实现（上）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="20&#32;结束语：Sentinel&#32;对应用的性能影响如何？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4359945a0a645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E6%B7%B1%E5%85%A5%E7%90%86%E8%A7%A3%20Sentinel%EF%BC%88%E5%AE%8C%EF%BC%89/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
