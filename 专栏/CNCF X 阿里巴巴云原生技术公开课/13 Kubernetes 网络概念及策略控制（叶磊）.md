<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>13 Kubernetes 网络概念及策略控制（叶磊）.md</title>
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

                    
                    <a href="01&#32;第一堂“云原生”课.md">01 第一堂“云原生”课.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;容器基本概念.md">02 容器基本概念.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;Kubernetes&#32;核心概念.md">03 Kubernetes 核心概念.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;理解&#32;Pod&#32;和容器设计模式.md">04 理解 Pod 和容器设计模式.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;应用编排与管理：核心原理.md">05 应用编排与管理：核心原理.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;应用编排与管理.md">06 应用编排与管理.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;应用编排与管理：Job&#32;&amp;&#32;DaemonSet.md">07 应用编排与管理：Job &amp; DaemonSet.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;应用配置管理.md">08 应用配置管理.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;应用存储和持久化数据卷：核心知识.md">09 应用存储和持久化数据卷：核心知识.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;应用存储和持久化数据卷：存储快照与拓扑调度(至天).md">10 应用存储和持久化数据卷：存储快照与拓扑调度(至天).md</a>

                </li>
                <li>

                    
                    <a href="11&#32;可观测性：你的应用健康吗？（莫源）.md">11 可观测性：你的应用健康吗？（莫源）.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;可观测性-监控与日志（莫源）.md">12 可观测性-监控与日志（莫源）.md</a>

                </li>
                <li>

                    <a class="current-tab" href="13&#32;Kubernetes&#32;网络概念及策略控制（叶磊）.md">13 Kubernetes 网络概念及策略控制（叶磊）.md</a>
                    

                </li>
                <li>

                    
                    <a href="14&#32;Kubernetes&#32;Service（溪恒）.md">14 Kubernetes Service（溪恒）.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;从&#32;0&#32;开始创作云原生应用（殷达）.md">15 从 0 开始创作云原生应用（殷达）.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;深入解析&#32;Linux&#32;容器（华敏）.md">16 深入解析 Linux 容器（华敏）.md</a>

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
                        <div><h1>13 Kubernetes 网络概念及策略控制（叶磊）</h1>
<p>本文将主要分享以下 5 方面的内容：</p>
<ol>
<li>Kubernetes 基本网络模型；</li>
<li>Netns 探秘；</li>
<li>主流网络方案简介；</li>
<li>Network Policy 的用处；</li>
<li>思考时间。</li>
</ol>
<h2>Kubernetes 基本网络模型</h2>
<p>本节来介绍一下 Kubernetes 对网络模型的一些想法。大家知道 Kubernetes 对于网络具体实现方案，没有什么限制，也没有给出特别好的参考案例。Kubernetes 对一个容器网络是否合格做出了限制，也就是 Kubernetes 的容器网络模型。可以把它归结为约法三章和四大目标。</p>
<ul>
<li>约法三章的意思是：在评价一个容器网络或者设计容器网络的时候，它的准入条件。它需要满足哪三条？ 才能认为它是一个合格的网络方案。</li>
<li>四大目标意思是在设计这个网络的拓扑，设计网络的具体功能的实现的时候，要去想清楚，能不能达成连通性等这几大指标。</li>
</ul>
<h3>约法三章</h3>
<p>先来看下约法三章：</p>
<ul>
<li>第一条：任意两个 pod 之间其实是可以直接通信的，无需经过显式地使用 NAT 来接收数据和地址的转换；</li>
<li>第二条：node 与 pod 之间是可以直接通信的，无需使用明显的地址转换；</li>
<li>第三条：pod 看到自己的 IP 跟别人看见它所用的IP是一样的，中间不能经过转换。</li>
</ul>
<p>后文中会讲一下我个人的理解，为什么 Kubernetes 对容器网络会有一些看起来武断的模型和要求。</p>
<h3>四大目标</h3>
<p>四大目标其实是在设计一个 K8s 的系统为外部世界提供服务的时候，从网络的角度要想清楚，外部世界如何一步一步连接到容器内部的应用？</p>
<ul>
<li>**外部世界和 service 之间是怎么通信的？**就是有一个互联网或者是公司外部的一个用户，怎么用到 service？service 特指 K8s 里面的服务概念。</li>
<li><strong>service 如何与它后端的 pod 通讯？</strong></li>
<li><strong>pod 和 pod 之间调用是怎么做到通信的？</strong></li>
<li><strong>最后就是 pod 内部容器与容器之间的通信？</strong></li>
</ul>
<p>最终要达到目标，就是外部世界可以连接到最里面，对容器提供服务。</p>
<h3>对基本约束的解释</h3>
<p>对基本约束，可以做出这样一些解读：因为容器的网络发展复杂性就在于它其实是寄生在 Host 网络之上的。从这个角度讲，可以把容器网络方案大体分为 <strong>Underlay/Overlay</strong> 两大派别：</p>
<ul>
<li>
<p>Underlay 的标准是它与 Host 网络是同层的，从外在可见的一个特征就是它是不是使用了 Host 网络同样的网段、输入输出基础设备、容器的 IP 地址是不是需要与 Host 网络取得协同（来自同一个中心分配或统一划分）。这就是 Underlay；</p>
</li>
<li>
<p>Overlay 不一样的地方就在于它并不需要从 Host 网络的 IPM 的管理的组件去申请IP，一般来说，它只需要跟 Host 网络不冲突，这个 IP 可以自由分配的。</p>
<p><img src="assets/Fhz1xeIxAKpYT30nYTMDPEe2fsKF" alt="avatar" /></p>
</li>
</ul>
<p>为什么社区会提出 perPodperIP 这种简单武断的模型呢？我个人是觉得这样为后面的 service 管理一些服务的跟踪性能监控，带来了非常多的好处。因为一个 IP 一贯到底，对 case 或者各种不大的事情都会有很大的好处。</p>
<h2>Netns 探秘</h2>
<h3>Netns 究竟实现了什么</h3>
<p>下面简单讲一下，Network Namespace 里面能网络实现的内核基础。狭义上来说 runC 容器技术是不依赖于任何硬件的，它的执行基础就是它的内核里面，进程的内核代表就是 task，它如果不需要隔离，那么用的是主机的空间（ namespace），并不需要特别设置的空间隔离数据结构（ nsproxy-namespace proxy）。</p>
<p><img src="assets/FoojsS015WB_S-B_daEr2ho1gSa4" alt="avatar" /></p>
<p>相反，如果一个独立的网络 proxy，或者 mount proxy，里面就要填上真正的私有数据。它可以看到的数据结构如上图所示。</p>
<p>从感官上来看一个隔离的网络空间，它会拥有自己的网卡或者说是网络设备。网卡可能是虚拟的，也可能是物理网卡，它会拥有自己的 IP 地址、IP 表和路由表、拥有自己的协议栈状态。这里面特指就是 TCP/Ip协议栈，它会有自己的status，会有自己的 iptables、ipvs。</p>
<p>从整个感官上来讲，这就相当于拥有了一个完全独立的网络，它与主机网络是隔离的。当然协议栈的代码还是公用的，只是数据结构不相同。</p>
<h3>Pod 与 Netns 的关系</h3>
<p><img src="assets/Fhtlyi6PUwJHW4e1-BJTtaXuPl6B" alt="avatar" /></p>
<p>这张图可以清晰表明 pod 里 Netns 的关系，每个 pod 都有着独立的网络空间，pod net container 会共享这个网络空间。一般 K8s 会推荐选用 Loopback 接口，在 pod net container 之间进行通信，而所有的 container 通过 pod 的 IP 对外提供服务。另外对于宿主机上的 Root Netns，可以把它看做一个特殊的网络空间，只不过它的 Pid 是1。</p>
<h2>主流网络方案简介</h2>
<h3>典型的容器网络实现方案</h3>
<p>接下来简单介绍一下典型的容器网络实现方案。容器网络方案可能是 K8s 里最为百花齐放的一个领域，它有着各种各样的实现。容器网络的复杂性，其实在于它需要跟底层 Iass 层的网络做协调、需要在性能跟 IP 分配的灵活性上做一些选择，这个方案是多种多样的。</p>
<p><img src="assets/FmJ42-sGp6Jlcmht2-KScPPIoos5" alt="avatar" /></p>
<p>下面简单介绍几个比较主要的方案：分别是 Flannel、Calico、Canal ，最后是 WeaveNet，中间的大多数方案都是采用了跟 Calico 类似的策略路由的方法。</p>
<ul>
<li><strong>Flannel</strong> 是一个比较大一统的方案，它提供了多种的网络 backend。不同的 backend 实现了不同的拓扑，它可以覆盖多种场景；</li>
<li><strong>Calico</strong> 主要是采用了策略路由，节点之间采用 BGP 的协议，去进行路由的同步。它的特点是功能比较丰富，尤其是对 Network Point 支持比较好，大家都知道 Calico 对底层网络的要求，一般是需要 mac 地址能够直通，不能跨二层域；</li>
<li>当然也有一些社区的同学会把 Flannel 的优点和 Calico 的优点做一些集成。我们称之为嫁接型的创新项目 <strong>Cilium</strong>；</li>
<li>最后讲一下 <strong>WeaveNet</strong>，如果大家在使用中需要对数据做一些加密，可以选择用 WeaveNet，它的动态方案可以实现比较好的加密。</li>
</ul>
<h3>Flannel 方案</h3>
<p><img src="assets/FhssEuWNm9DD-eRNnc51NNkEObNb" alt="avatar" /></p>
<p>Flannel 方案是目前使用最为普遍的。如上图所示，可以看到一个典型的容器网方案。它首先要解决的是 container 的包如何到达 Host，这里采用的是加一个 Bridge 的方式。它的 backend 其实是独立的，也就是说这个包如何离开 Host，是采用哪种封装方式，还是不需要封装，都是可选择的。</p>
<p>现在来介绍三种主要的 backend：</p>
<ul>
<li>一种是用户态的 udp，这种是最早期的实现；</li>
<li>然后是内核的 Vxlan，这两种都算是 overlay 的方案。Vxlan 的性能会比较好一点，但是它对内核的版本是有要求的，需要内核支持 Vxlan 的特性功能；</li>
<li>如果你的集群规模不够大，又处于同一个二层域，也可以选择采用 host-gw 的方式。这种方式的 backend 基本上是由一段广播路由规则来启动的，性能比较高。</li>
</ul>
<h2>Network Policy 的用处</h2>
<h3>Network Policy 基本概念</h3>
<p>下面介绍一下 Network Policy 的概念。</p>
<p><img src="assets/FgcMnXjYQ4VCi7tdl6TY-gcIFJBY" alt="avatar" /></p>
<p>刚才提到了 Kubernetes 网络的基本模型是需要 pod 之间全互联，这个将带来一些问题：可能在一个 K8s 集群里，有一些调用链之间是不会直接调用的。比如说两个部门之间，那么我希望 A 部门不要去探视到 B 部门的服务，这个时候就可以用到策略的概念。</p>
<p>基本上它的想法是这样的：它采用各种选择器（标签或 namespace），找到一组 pod，或者找到相当于通讯的两端，然后通过流的特征描述来决定它们之间是不是可以联通，可以理解为一个白名单的机制。</p>
<p>在使用 Network Policy 之前，如上图所示要注意 apiserver 需要打开一下这几个开关。另一个更重要的是我们选用的网络插件需要支持 Network Policy 的落地。大家要知道，Network Policy 只是 K8s 提供的一种对象，并没有内置组件做落地实施，需要取决于你选择的容器网络方案对这个标准的支持与否及完备程度，如果你选择 Flannel 之类，它并没有真正去落地这个 Policy，那么你试了这个也没有什么用。</p>
<h3>配置实例</h3>
<p><img src="assets/Fveji-UPz0yJjDG1dsDW3zqBikeT" alt="avatar" /></p>
<p>接下来讲一个配置的实例，或者说在设计一个 Network Policy 的时候要做哪些事情？我个人觉得需要决定三件事：</p>
<ul>
<li>第一件事是控制对象，就像这个实例里面 spec 的部分。spec 里面通过 podSelector 或者 namespace 的 selector，可以选择做特定的一组 pod 来接受我们的控制；</li>
<li>第二个就是对流向考虑清楚，需要控制入方向还是出方向？还是两个方向都要控制？</li>
<li>最重要的就是第三部分，如果要对选择出来的方向加上控制对象来对它流进行描述，具体哪一些 stream 可以放进来，或者放出去？类比这个流特征的五元组，可以通过一些选择器来决定哪一些可以作为我的远端，这是对象的选择；也可以通过 IPBlock 这种机制来得到对哪些 IP 是可以放行的；最后就是哪些协议或哪些端口。其实流特征综合起来就是一个五元组，会把特定的能够接受的流选择出来 。</li>
</ul>
<h2>本节课总结</h2>
<p>本节内容到这里就结束了，我们简单总结一下：</p>
<ul>
<li>
<p>在 pod 的容器网络中核心概念就是 IP，IP 就是每个 pod 对外通讯的地址基础，必须内外一致，符合 K8s 的模型特征；</p>
</li>
<li>
<p>那么在介绍网络方案的时候，影响容器网络性能最关键的就是拓扑。要能够理解你的包端到端是怎么联通的，中间怎么从 container 到达 Host，Host 出了 container 是要封装还是解封装？还是通过策略路由？最终到达对端是怎么解出来的？</p>
</li>
<li>
<p>容器网络选择和设计选择。如果你并不清楚你的外部网络，或者你需要一个普适性最强的方案，假设说你对 mac 是否直连不太清楚、对外部路由器的路由表能否控制也不太清楚，那么你可以选择 Flannel 利用 Vxlan 作为 backend 的这种方案。如果你确信你的网络是 2 层可直连的，你可以进行选用 Calico 或者 Flannel-Hostgw 作为一个 backend；</p>
</li>
<li>
<p>最后就是对 Network Policy，在运维和使用的时候，它是一个很强大的工具，可以实现对进出流的精确控制。实现的方法我们也介绍了，要想清楚你要控制谁，然后你的流要怎么去定义。</p>
</li>
</ul>
<h2>思考时间</h2>
<p>最后留一些思考，大家可以想一想：</p>
<ol>
<li>为什么接口标准化 CNI 化了，但是容器网络却没有一个很标准的实现，内置在 K8s 里面？</li>
<li>Network Policy 为什么没有一个标准的 controller 或者一个标准的实现，而是交给这个容器网络的 owner 来提供？</li>
<li>有没有可能完全不用网络设备来实现容器网络呢？考虑到现在有 RDMA 等有别于 TCP/IP 的这种方案。</li>
<li>在运维过程中网络问题比较多、也比较难排查，那么值不值得做一个开源工具，让它可以友好的展示从 container 到 Host 之间、Host 到 Host 之间，或者说封装及解封装之间，各个阶段的网络情况，有没有出现问题，能够快速的定位。据我所知应该现在是没有这样的工具的。</li>
</ol>
<p>以上就是我对 K8s 容器网络的基本概念、以及 Network Policy 的一些介绍，谢谢大家的观看。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="12&#32;可观测性-监控与日志（莫源）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="14&#32;Kubernetes&#32;Service（溪恒）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433de68e3970ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/CNCF%20X%20%E9%98%BF%E9%87%8C%E5%B7%B4%E5%B7%B4%E4%BA%91%E5%8E%9F%E7%94%9F%E6%8A%80%E6%9C%AF%E5%85%AC%E5%BC%80%E8%AF%BE/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
