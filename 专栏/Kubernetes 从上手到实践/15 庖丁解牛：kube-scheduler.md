<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>15 庖丁解牛：kube-scheduler.md</title>
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

                    
                    <a href="01&#32;&#32;开篇：&#32;Kubernetes&#32;是什么以及为什么需要它.md">01  开篇： Kubernetes 是什么以及为什么需要它.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;初步认识：Kubernetes&#32;基础概念.md">02 初步认识：Kubernetes 基础概念.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;宏观认识：整体架构.md">03 宏观认识：整体架构.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;搭建&#32;Kubernetes&#32;集群&#32;-&#32;本地快速搭建.md">04 搭建 Kubernetes 集群 - 本地快速搭建.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;动手实践：搭建一个&#32;Kubernetes&#32;集群&#32;-&#32;生产可用.md">05 动手实践：搭建一个 Kubernetes 集群 - 生产可用.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;集群管理：初识&#32;kubectl.md">06 集群管理：初识 kubectl.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;集群管理：以&#32;Redis&#32;为例-部署及访问.md">07 集群管理：以 Redis 为例-部署及访问.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;安全重点&#32;认证和授权.md">08 安全重点 认证和授权.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;应用发布：部署实际项目.md">09 应用发布：部署实际项目.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;应用管理：初识&#32;Helm.md">10 应用管理：初识 Helm.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;部署实践：以&#32;Helm&#32;部署项目.md">11 部署实践：以 Helm 部署项目.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;庖丁解牛：kube-apiserver.md">12 庖丁解牛：kube-apiserver.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;庖丁解牛：etcd.md">13 庖丁解牛：etcd.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;庖丁解牛：controller-manager.md">14 庖丁解牛：controller-manager.md</a>

                </li>
                <li>

                    <a class="current-tab" href="15&#32;庖丁解牛：kube-scheduler.md">15 庖丁解牛：kube-scheduler.md</a>
                    

                </li>
                <li>

                    
                    <a href="16&#32;庖丁解牛：kubelet.md">16 庖丁解牛：kubelet.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;庖丁解牛：kube-proxy.md">17 庖丁解牛：kube-proxy.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;庖丁解牛：Container&#32;Runtime&#32;（Docker）.md">18  庖丁解牛：Container Runtime （Docker）.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;Troubleshoot.md">19 Troubleshoot.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;扩展增强：Dashboard.md">20 扩展增强：Dashboard.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;扩展增强：CoreDNS.md">21 扩展增强：CoreDNS.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;服务增强：Ingress.md">22 服务增强：Ingress.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;监控实践：对&#32;K8S&#32;集群进行监控.md">23 监控实践：对 K8S 集群进行监控.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;总结.md">24 总结.md</a>

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
                        <div><h1>15 庖丁解牛：kube-scheduler</h1>
<h2>整体概览</h2>
<pre><code>+----------------------------------------------------------+          
| Master                                                   |          
|              +-------------------------+                 |          
|     +-------&gt;|        API Server       |&lt;--------+       |          
|     |        |                         |         |       |          
|     v        +-------------------------+         v       |          
|   +----------------+     ^      +--------------------+   |          
|   |                |     |      |                    |   |          
|   |   Scheduler    |     |      | Controller Manager |   |          
|   |                |     |      |                    |   |          
|   +----------------+     v      +--------------------+   |          
| +------------------------------------------------------+ |          
| |                                                      | |          
| |                Cluster state store                   | |          
| |                                                      | |          
| +------------------------------------------------------+ |          
+----------------------------------------------------------+          
</code></pre>
<p>在第 3 节《宏观认识：整体架构》 中，我们也认识到了 <code>Scheduler</code> 的存在，知道了 Master 是 K8S 是集群的大脑，<code>Controller Manager</code> 负责将集群调整至预期的状态，而 <code>Scheduler</code> 则是集群调度器，将预期的 <code>Pod</code> 资源调度到正确的 <code>Node</code> 节点上，进而令该 <code>Pod</code> 可完成启动。本节我们一同来看看它如何发挥如此大的作用。</p>
<p><strong>下文统一使用 kube-scheduler 进行表述</strong></p>
<h2><code>kube-scheduler</code> 是什么</h2>
<p>引用<a href="https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/">官方文档</a>一句话：</p>
<blockquote>
<p>The Kubernetes scheduler is a policy-rich, topology-aware, workload-specific function that significantly impacts availability, performance, and capacity.</p>
</blockquote>
<p><code>kube-scheduler</code> 是一个策略丰富，拓扑感知的调度程序，会显著影响可用性，性能和容量。</p>
<p>我们知道资源调度本就是 K8S 这类系统中的一个很复杂的事情，既要能满足系统对资源利用率的需要，同样还需要避免资源竞争，比如说端口冲突之类的。</p>
<p>为了能完成这样的需求，<code>kube-scheduler</code> 便在不断的迭代和发展，通过支持多种策略满足各类需求，通过感知拓扑避免资源竞争和保障系统的可用性及容量等。</p>
<p>我们在第 5 节下载服务端二进制文件解压后，便可看到 <code>kube-scheduler</code> 的可执行文件。当给它传递 <code>--help</code> 查看其支持参数的时候，便可以看到它支持使用 <code>--address</code> 或者 <code>--bind-address</code> 等参数指定所启动的 HTTP server 所绑定的地址之类的。</p>
<p>它和 <code>kube-controller-manager</code> 有点类似，同样是通过定时的向 <code>kube-apiserver</code> 请求获取信息，并进行处理。而他们所起到的作用并不相同。</p>
<h2><code>kube-scheduler</code> 有什么作用</h2>
<p>从上层的角度来看，<code>kube-scheduler</code> 的作用就是将待调度的 <code>Pod</code> 调度至最佳的 <code>Node</code> 上，而这个过程中则需要根据不同的策略，考虑到 <code>Node</code> 的资源使用情况，比如端口，内存，存储等。</p>
<h2><code>kube-scheduler</code> 是如何工作的</h2>
<p>整体的过程可通过 <code>pkg/scheduler/core/generic_scheduler.go</code> 的代码来看</p>
<pre><code>func (g *genericScheduler) Schedule(pod *v1.Pod, nodeLister algorithm.NodeLister) (string, error) {
	trace := utiltrace.New(fmt.Sprintf(&quot;Scheduling %s/%s&quot;, pod.Namespace, pod.Name))
	defer trace.LogIfLong(100 * time.Millisecond)

	if err := podPassesBasicChecks(pod, g.pvcLister); err != nil {
		return &quot;&quot;, err
	}

	nodes, err := nodeLister.List()
	if err != nil {
		return &quot;&quot;, err
	}
	if len(nodes) == 0 {
		return &quot;&quot;, ErrNoNodesAvailable
	}

	err = g.cache.UpdateNodeNameToInfoMap(g.cachedNodeInfoMap)
	if err != nil {
		return &quot;&quot;, err
	}

	trace.Step(&quot;Computing predicates&quot;)
	startPredicateEvalTime := time.Now()
	filteredNodes, failedPredicateMap, err := g.findNodesThatFit(pod, nodes)
	if err != nil {
		return &quot;&quot;, err
	}

	if len(filteredNodes) == 0 {
		return &quot;&quot;, &amp;FitError{
			Pod:              pod,
			NumAllNodes:      len(nodes),
			FailedPredicates: failedPredicateMap,
		}
	}
	metrics.SchedulingAlgorithmPredicateEvaluationDuration.Observe(metrics.SinceInMicroseconds(startPredicateEvalTime))
	metrics.SchedulingLatency.WithLabelValues(metrics.PredicateEvaluation).Observe(metrics.SinceInSeconds(startPredicateEvalTime))

	trace.Step(&quot;Prioritizing&quot;)
	startPriorityEvalTime := time.Now()
	// When only one node after predicate, just use it.
	if len(filteredNodes) == 1 {
		metrics.SchedulingAlgorithmPriorityEvaluationDuration.Observe(metrics.SinceInMicroseconds(startPriorityEvalTime))
		return filteredNodes[0].Name, nil
	}

	metaPrioritiesInterface := g.priorityMetaProducer(pod, g.cachedNodeInfoMap)
	priorityList, err := PrioritizeNodes(pod, g.cachedNodeInfoMap, metaPrioritiesInterface, g.prioritizers, filteredNodes, g.extenders)
	if err != nil {
		return &quot;&quot;, err
	}
	metrics.SchedulingAlgorithmPriorityEvaluationDuration.Observe(metrics.SinceInMicroseconds(startPriorityEvalTime))
	metrics.SchedulingLatency.WithLabelValues(metrics.PriorityEvaluation).Observe(metrics.SinceInSeconds(startPriorityEvalTime))

	trace.Step(&quot;Selecting host&quot;)
	return g.selectHost(priorityList)
}
</code></pre>
<p>它的输入有两个：</p>
<ul>
<li><code>pod</code>：待调度的 <code>Pod</code> 对象；</li>
<li><code>nodeLister</code>：所有可用的 <code>Node</code> 列表</li>
</ul>
<p>备注：<code>nodeLister</code> 的实现稍微用了点技巧，返回的是 <code>[]*v1.Node</code> 而不是 <code>v1.NodeList</code> 可避免拷贝带来的性能损失。</p>
<pre><code>type NodeLister interface {
	List() ([]*v1.Node, error)
}
</code></pre>
<h3>处理阶段</h3>
<p><code>kube-scheduler</code> 将处理阶段主要分为三个阶段 <code>Computing predicates</code>，<code>Prioritizing</code>和 <code>Selecting host</code>：</p>
<ul>
<li>
<p><code>Computing predicates</code>：主要解决的问题是 <code>Pod</code> 能否调度到集群的 <code>Node</code> 上；</p>
<p>主要是通过一个名为 <code>podFitsOnNode</code> 的函数进行实现，在检查的过程中也会先去检查下是否已经有已缓存的判断结果， 当然也会检查 <code>Pod</code> 是否是可调度的，以防有 <code>Pod Affinity</code> (亲合性) 之类的存在。</p>
</li>
<li>
<p><code>Prioritizing</code>：主要解决的问题是在上个阶段通过 <code>findNodesThatFit</code> 得到了 <code>filteredNodes</code> 的基础之上解决哪些 <code>Node</code> 是最优的，得到一个优先级列表 <code>priorityList</code>;</p>
<p>至于优先级的部分，主要是通过下面的代码：</p>
<pre><code>for i := range nodes {
	result = append(result, schedulerapi.HostPriority{Host: nodes[i].Name, Score: 0})
	for j := range priorityConfigs {
		result[i].Score += results[j][i].Score * priorityConfigs[j].Weight
	}
}
</code></pre>
<p>给每个经过第一步筛选出来的 <code>Node</code> 一个 <code>Score</code>，再按照各种条件进行打分，最终得到一个优先级列表。</p>
</li>
<li>
<p><code>Selecting host</code>：则是最终选择 <code>Node</code> 调度到哪台机器上。</p>
<p>最后，则是通过 <code>selectHost</code> 选择出最终要调度到哪台机器上。</p>
<pre><code>func (g *genericScheduler) selectHost(priorityList schedulerapi.HostPriorityList) (string, error) {
    if len(priorityList) == 0 {
        return &quot;&quot;, fmt.Errorf(&quot;empty priorityList&quot;)
    }

    sort.Sort(sort.Reverse(priorityList))
    maxScore := priorityList[0].Score
    firstAfterMaxScore := sort.Search(len(priorityList), func(i int) bool { return priorityList[i].Score &lt; maxScore })

    g.lastNodeIndexLock.Lock()
    ix := int(g.lastNodeIndex % uint64(firstAfterMaxScore))
    g.lastNodeIndex++
    g.lastNodeIndexLock.Unlock()

    return priorityList[ix].Host, nil
}
</code></pre>
</li>
</ul>
<h2>总结</h2>
<p>在本节中，我们介绍了 <code>kube-scheduler</code> 以及它在调度 <code>Pod</code> 的过程中的大致步骤。</p>
<p>不过它实际使用的各种策略及判断条件很多，无法在一节中完全都详细介绍，感兴趣的朋友可以按照本节中提供的思路大致去看看它的实现。</p>
<p>我们通过前面几节的介绍，已经知道了当实际进行部署操作的时候，首先会通过 <code>kubectl</code> 之类的客户端工具与 <code>kube-apiserver</code> 进行交互，在经过一系列的处理后，数据将持久化到 <code>etcd</code> 中；</p>
<p>此时，<code>kube-controller-manager</code> 通过持续的观察，开始按照我们的配置，将集群的状态调整至预期状态；</p>
<p>而 <code>kube-scheduler</code> 也在发挥作用，决定 <code>Pod</code> 应该调度至哪个或者哪些 <code>Node</code> 上；之后则通过其他组件的协作，最总将该 <code>Pod</code> 在相应的 <code>Node</code> 上部署启动。</p>
<p>我们在下节将要介绍的 <code>kubelet</code> 便是后面这部分“实际部署动作”相关的组件中尤为重要的一个，下节我们再详细介绍它是如何完成这些功能的。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="14&#32;庖丁解牛：controller-manager.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="16&#32;庖丁解牛：kubelet.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43460ea99270ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Kubernetes%20%E4%BB%8E%E4%B8%8A%E6%89%8B%E5%88%B0%E5%AE%9E%E8%B7%B5/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
