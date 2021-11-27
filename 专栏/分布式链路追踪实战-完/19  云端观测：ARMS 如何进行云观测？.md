<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>19  云端观测：ARMS 如何进行云观测？.md</title>
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

                    
                    <a href="00&#32;分布式链路追踪实战.md">00 分布式链路追踪实战.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;数据观测：数据追踪的基石从哪里来？.md">01  数据观测：数据追踪的基石从哪里来？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;系统日志：何以成为保障稳定性的关键？.md">02  系统日志：何以成为保障稳定性的关键？.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;日志编写：怎样才能编写“可观测”的系统日志？.md">03  日志编写：怎样才能编写“可观测”的系统日志？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;统计指标：“五个九”对系统稳定的真正意义.md">04  统计指标：“五个九”对系统稳定的真正意义.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;监控指标：如何通过分析数据快速定位系统隐患？（上）.md">05  监控指标：如何通过分析数据快速定位系统隐患？（上）.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;监控指标：如何通过分析数据快速定位系统隐患？（下）.md">06  监控指标：如何通过分析数据快速定位系统隐患？（下）.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;指标编写：如何编写出更加了解系统的指标？.md">07  指标编写：如何编写出更加了解系统的指标？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;链路监控：为什么对于系统而言必不可少？.md">08  链路监控：为什么对于系统而言必不可少？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;性能剖析：如何补足分布式追踪短板？.md">09  性能剖析：如何补足分布式追踪短板？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;链路分析：除了观测链路，还能做什么？.md">10  链路分析：除了观测链路，还能做什么？.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;黑白盒监控：系统功能与结构稳定的根基.md">11  黑白盒监控：系统功能与结构稳定的根基.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;系统告警：快速感知业务隐藏问题.md">12  系统告警：快速感知业务隐藏问题.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;告警质量：如何更好地创建告警规则和质量？.md">13  告警质量：如何更好地创建告警规则和质量？.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;告警处理：怎样才能更好地解决问题？.md">14  告警处理：怎样才能更好地解决问题？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;日志收集：ELK&#32;如何更高效地收集日志？.md">15  日志收集：ELK 如何更高效地收集日志？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;指标体系：Prometheus&#32;如何更完美地显示指标体系？.md">16  指标体系：Prometheus 如何更完美地显示指标体系？.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;链路追踪：Zipkin&#32;如何进行分布式追踪？.md">17  链路追踪：Zipkin 如何进行分布式追踪？.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;观测分析：SkyWalking&#32;如何把观测和分析结合起来？.md">18  观测分析：SkyWalking 如何把观测和分析结合起来？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="19&#32;&#32;云端观测：ARMS&#32;如何进行云观测？.md">19  云端观测：ARMS 如何进行云观测？.md</a>
                    

                </li>
                <li>

                    
                    <a href="20&#32;&#32;运维集成：内部的&#32;OSS&#32;系统如何与观测相结合？.md">20  运维集成：内部的 OSS 系统如何与观测相结合？.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;结束语&#32;&#32;未来的监控是什么样子？.md">21 结束语  未来的监控是什么样子？.md</a>

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
                        <div><h1>19  云端观测：ARMS 如何进行云观测？</h1>
<p>上一节，我带你了解了链路追踪中的关键功能，链路分析，以及它在 Skywalking 中的原理和实践。在这一节，我将带你了解云观测。</p>
<h3>功能</h3>
<p>随着用户流量、业务系统的复杂化，单一的服务器已经无法再满足我们的业务需求。机器数量越来越多，传统的自建服务器很难做到良好的维护，从而便衍生出了云服务器的概念。</p>
<p>云服务器利用云服务商提供的云主机替代了原先公司自建的主机，减少了公司购买主机、维护主机的成本。同时，云服务商还可以利用自己的研发能力，提供一套属于自己的基础组件，简化运维人员在运维基础组件时的成本、研发也无需再关心技术选型，只需要使用这个组件，让研发真正做到了只关心业务。</p>
<p>基于这些原因，目前已经有很多公司把自己的服务搬到云上运行。</p>
<p>但是随之而来有一个问题，如何在云上进行监控呢？现在很多云厂商对应自己的组件，都有一套自己的可观测方案，无论是哪一种方案，都能起到<strong>端到端观测</strong>、<strong>全栈性能监控</strong>、<strong>方案统一</strong>、<strong>统一观测</strong>这 4 个作用。</p>
<ol>
<li><strong>端到端观测</strong>：帮助你实现从 App、Web 页面、H5 端到后端服务器端的全流程、全链路的监控。因为服务是在云上运行的，所以云服务商可以将基础数据一并整合，帮你做到全方位地了解。</li>
<li><strong>全栈性能监控</strong>：因为云上会有各种各样的公司，会接入各种各样的语言，那么它必然会考虑到不同的应用场景。此时，云观测系统则会适配不同的语言对全栈的应用都提供性能监控。</li>
<li><strong>方案统一</strong>：由于云厂商一般都会提供一整套完整的组件库，比如阿里云的文件存储系统、消息队列等服务；也包含像视频点播、对象存储等对应特定场景的解决方案。通过云厂商提供的云观测，可以无缝地和其他系统对接，让你能快速了解每个组件和方案内部的细节。</li>
<li><strong>统一观测</strong>：由于业务系统和组件都部署在云端，我们可以将可观测性中的每一个部分都接入云服务，包括日志、统计指标和链路追踪，依靠云服务来进行整合，通过云服务整合的方式，你无需再事无巨细地关心每一类数据是怎样上报，怎样整合的。</li>
</ol>
<h3>ARMS</h3>
<p>阿里云提供的 ARMS 就是包含上述功能的一套云观测系统，除了以上 4 点，它还提供了很多特有的功能，让你更方便地观测数据。</p>
<h4>提供功能</h4>
<p>ARMS 提供的功能主要分为 6 个部分：前端监控、App 监控、应用监控、自定义监控、大盘展示、报警。我们依次来看。</p>
<p><img src="assets/CgqCHl9y50CAXyttAAEVMU02lVM306.png" alt="Lark20200929-154947.png" /></p>
<p><strong>前端监控</strong>
<strong>前端监控指的是通过在页面中埋入脚本的形式，让阿里云接管前端的数据上报</strong>。其中就包含我们比较常见的脚本错误次数、接口请求次数、PV、UV 等统计数据，也包含页面中脚本错误、API 访问等数据信息。通过统计数据你能快速了解前端用户的访问情况；脚本错误、API 访问等数据，则可以帮助你了解页面出现错误或者接口访问时的详细信息。</p>
<p><strong>App 监控</strong>
<strong>App 监控的接入方式与前端监控方式类似，都是通过增加相关 SDK 的方式添加监控</strong>。其中主要包含崩溃、性能分析和远程日志获取。</p>
<ul>
<li><strong>崩溃指标和日志</strong>可以帮助移动端研发人员了解相关崩溃率，可以及时掌握崩溃时的堆栈信息，用于快速定位问题。</li>
<li><strong>性能分析</strong>可以帮助研发人员了解页面中的统计指标，比如卡顿率、启动时间，从而得知当前 App 的性能处在什么水平。</li>
<li><strong>远程日志</strong>则可以收集存储在每个用户手机中的 App 操作日志。研发人员能够根据这部分日志分析复杂场景下用户使用的问题，并深入到具体的用户维度查看问题。</li>
</ul>
<p><strong>应用监控</strong>
ARMS 的应用监控和我之前讲的链路追踪的内容十分相似，其中就包含链路数据查询，与业务系统的日志结合，统计指标、拓扑图等信息。阿里云的应用监控还提供了根据参数查询链路的功能，可以在链路中增加业务属性，让你在查询问题链路时更加个性化。</p>
<p>将链路追踪放到云平台的有一个好处，那就是它可以和内部系统做完整的集成，比如结合阿里云提供的全生态组件，查看相互之间的全链路。</p>
<p><strong>自定义监控</strong>
自定义监控提供多种场景的数据内容的自定义解析、数据清洗、聚合、保存到统计指标中，进行监控告警。</p>
<p>一般数据源都是通过日志的方式输入，我们可以根据日志中统一的规定，比如限定具体用户 ID 字段的解析位置，去计算异常次数、访问次数等数据。这样的方式可以方便你进行业务层的数据分析，与业务结合起来可以让你不再局限于技术层面去思考问题。</p>
<p><strong>大盘展示</strong>
根据指标数据内容定制显示大盘数据。通过定制化的方式，你可以将系统中已有的统计指标内容，通过定制化的图表展示。</p>
<p>你可以能够通过页面的方式，快速了解关心的业务的实时情况。阿里巴巴“双十一”时的交易额页面上会显示实时的交易额，也会显示一些国内外的主要指标数据，这个就是大盘展示最典型的应用场景。</p>
<p><strong>报警</strong>
与我在“<strong>模块二</strong>”中讲到的创建规则与告警十分相似。阿里云 ARMS 所提供的告警功能，会提供一个界面，让你十分方便地通过这个界面去集成各个端中的数据和所有统计指标。同时，它也支持短信、钉钉、邮件等通知方式。</p>
<p><strong>端到端监控</strong>
下面，我们依次来看一下如何在 ARMS 上实践上面说到的前端监控、APP 监控和应用监控。</p>
<p><strong>前端监控</strong>
如上文所说，前端监控是通过在代码中增加脚本的方式来实现数据监控的。代码如下：</p>
<pre><code>!(function(c,b,d,a){c[a]||(c[a]={});c[a].config={pid:&quot;xx&quot;,AppType:&quot;web&quot;,imgUrl:&quot;https://arms-retcode.aliyuncs.com/r.png?&quot;,sendResource:true,enableLinkTrace:true,behavior:true};

  with(b)with(body)with(insertBefore(createElement(&quot;script&quot;),firstChild))setAttribute(&quot;crossorigin&quot;,&quot;&quot;,src=d)

})(window,document,&quot;https://retcode.alicdn.com/retcode/bl.js&quot;,&quot;__bl&quot;);
</code></pre>
<p>在页面中，通过 script 标签引入一个 JavaScript 文件来进行任务处理，然后通过 pid 参数设定的应用 ID，保证数据只会上传到你的服务中。</p>
<p><strong>网页运行时就会自动下载 bl.js 文件，下载完成后，代码会自动执行</strong>。当页面处理各种事件时，会通过异步的形式，上报当前的事件信息，从而实现对前端运行环境、执行情况的监控。常见的事件有：页面启动加载、页面加载完成、用户操作行为、页面执行时出现错误、离开页面。</p>
<p><strong>页面加载完成之后，会发送 HEAD 请求来上报数据</strong>。其中我们可以清楚的看到，在请求参数中包含 DNS、TCP、SSL、DOM、LOAD 等信息，分别代表 DNS 寻找、TCP 建立连接、SSL 握手这类，我在“<strong>05 | 监控指标：如何通过分析数据快速定位系统隐患？（上）</strong>”中讲到的通用指标，也包含 DOM 元素加载时间这类网页中的统计指标信息。如下所示：</p>
<p><img src="assets/CgqCHl9xdOCAJwMaAAFLBfVQzpI118.png" alt="1.png" /></p>
<p>数据上报后，ARMS 就会接收到相对应事件中的完整数据信息，从而通过聚合的方式，存储和展示数据。在 ARMS 中，针对应用有访问速度、JS 错误、API 请求这些统计指标和错误信息的数据，ARMS 可以依据不同维度的数据了解到更详细的内容，包含页面、地理、终端、网络这 4 类。通过不同的数据维度，你也可以更有针对性地了解问题。</p>
<p><strong>App 监控</strong>
App 的监控方式与前端监控十分类似，都需要通过增加代码的方式进行。以 iOS 为例，如果我们想要接入性能分析功能，除了要引入相关依赖，还需要在代码中进行如下的声明：</p>
<pre><code>[[AlicloudAPMProvider alloc] autoInitWithAppVersion:AppVersion channel:channel nick:nick];

[AlicloudHAProvider start];
</code></pre>
<p>这段代码会创建 AlicloudAPMProvider 对象，并且传入相关的参数，然后通过 start 方法启动监控功能。</p>
<p><strong>应用监控</strong>
对于服务端监控来说，ARMS 支持目前主流的 Java、PHP、Go 等语言，这里我以 Java 语言为例说明。</p>
<p>在 Java 中，主要通过字节码增强的形式采集数据。项目启动后，会采集机器中 JVM 中的统计指标、链路数据等信息，然后结合链路，分析出统计指标、拓扑图的信息，以及应用与各个组件之间的交互细节，比如数据库查询、消息 MQ 发送量等数据信息。</p>
<p>在服务端监控中，我们可以看到请求链路中的数据，在 ARMS 的显示中都是基于应用的维度，以树形进行展示的。比如我们有 2 个应用程序，上游服务通过“/first”接口地址对外提供服务，同时又调用了下游服务的“/second”接口。如下图所示：</p>
<p><img src="assets/Ciqc1F9xdSaAFrAgAACCWZpq9Zk452.png" alt="1.png" /></p>
<p>这张图中展示了对应的上下游服务、发生时间、实例地址、调用方式、服务名称和时间轴信息。并且我们可以通过点击其中单个服务的“方法栈”按钮，查看其链路中关键方法的执行流程。点开之后的页面如下：</p>
<p><img src="assets/CgqCHl9xdTaAZPFUAADXO6lzCSY138.png" alt="1.png" /></p>
<p><strong>在 ARMS 中服务端监控的功能中，最常用的是应用诊断部分，其中包含了实时诊断、异常分析、线程分析这 3 部分重点功能。</strong></p>
<ul>
<li><strong>实时诊断</strong>：默认情况下，服务端监控会通过采样的形式采集链路数据，以此来保证尽可能地减少对线上服务造成性能损耗。大多数情况下，指标数据都能快速体现出运行情况。在实时诊断中，会临时采取 100%采集，将所有的请求链路进行采集并上报，此时则可以看到指定时间段内的所有链路信息。</li>
</ul>
<p><img src="assets/Ciqc1F9xdZWAKUZzAAFEFkYvTqk447.png" alt="1.png" /></p>
<ul>
<li><strong>异常分析</strong>：汇总当前应用下存在的各种异常信息，你可以了解你的应用中哪些异常信息是相对较多的。有限优化占比较多的错误信息，有利于提升服务整体的成功率。</li>
</ul>
<p>下图中汇总了服务中出现错误的异常信息，我们可以通过点击具体的接口名称，找到对应的接口，更细致地查看接口细则。</p>
<p><img src="assets/Ciqc1F9xdbGAB7dKAAFsqvOFvIM738.png" alt="1.png" /></p>
<ul>
<li><strong>线程分析</strong>：列出当前应用实例中具体的线程或者线程池列表。我们可以根据线程数或者 CPU 耗时信息来对线程进行排序，更直观地看出哪个线程池中创建的线程比较多，或者具体哪个线程消耗 CPU 资源较多。</li>
</ul>
<p>如果程序出现执行缓慢的情况，我们可以通过 CPU 资源消耗来寻找原因。还可以通过点击每个线程中右侧的方法栈，来快速查看指定线程的执行方法栈信息。查询到问题的原因后，我们再结合具体的业务场景处理问题。</p>
<p><img src="assets/Ciqc1F9xdc6AJYAaAAGwMophZgc898.png" alt="1.png" /></p>
<h3>总结</h3>
<p>以上，我介绍了云端观测的作用以及在阿里云的 ARMS 系统中的实践。如果你的系统部署在云端，那么云端观测就是你进行系统观测的不二选择。你通过云端观测解决过哪些问题呢？欢迎你在留言区分享。</p>
<p>下一节，我将带你了解如何将可观测系统与 OSS 系统相结合。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="18&#32;&#32;观测分析：SkyWalking&#32;如何把观测和分析结合起来？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="20&#32;&#32;运维集成：内部的&#32;OSS&#32;系统如何与观测相结合？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4351a76f39645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E5%88%86%E5%B8%83%E5%BC%8F%E9%93%BE%E8%B7%AF%E8%BF%BD%E8%B8%AA%E5%AE%9E%E6%88%98-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
