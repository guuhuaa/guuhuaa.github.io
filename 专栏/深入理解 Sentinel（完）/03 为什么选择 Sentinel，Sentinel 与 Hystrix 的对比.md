<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>03 为什么选择 Sentinel，Sentinel 与 Hystrix 的对比.md</title>
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

                    <a class="current-tab" href="03&#32;为什么选择&#32;Sentinel，Sentinel&#32;与&#32;Hystrix&#32;的对比.md">03 为什么选择 Sentinel，Sentinel 与 Hystrix 的对比.md</a>
                    

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

                    
                    <a href="19&#32;Sentinel&#32;集群限流的实现（下）.md">19 Sentinel 集群限流的实现（下）.md</a>

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
                        <div><h1>03 为什么选择 Sentinel，Sentinel 与 Hystrix 的对比</h1>
<h3>为什么选择 Sentinel？</h3>
<p>选择 Sentinel 与 Hystrix 通常第一步都是通过对比两者优缺点，Sentinel 与 Hystrix 的对比结果是作为我们选择 Sentinel 还是 Hystrix 的直观参考，不过使用 Sentinel 能做什么，是否满足实际需求才是我们最终决定是否使用 Sentinel 的最关键因素，否则尽管一个框架再好，不适合也不会选择。</p>
<p>以下 Sentinel 与 Hystrix 的对比，表格来自 Sentinel Github 官方文档。</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Sentinel</th>
<th align="left">Hystrix</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">隔离策略</td>
<td align="left">信号量隔离</td>
<td align="left">线程池隔离/信号量隔离</td>
</tr>
<tr>
<td align="left">熔断降级策略</td>
<td align="left">基于响应时间或失败比率</td>
<td align="left">基于失败比率</td>
</tr>
<tr>
<td align="left">实时指标实现</td>
<td align="left">滑动窗口</td>
<td align="left">滑动窗口（基于 RxJava）</td>
</tr>
<tr>
<td align="left">规则配置</td>
<td align="left">支持多种数据源</td>
<td align="left">支持多种数据源</td>
</tr>
<tr>
<td align="left">扩展性</td>
<td align="left">多个 SPI 扩展点</td>
<td align="left">插件的形式</td>
</tr>
<tr>
<td align="left">基于注解的支持</td>
<td align="left">支持</td>
<td align="left">支持</td>
</tr>
<tr>
<td align="left">限流</td>
<td align="left">基于 QPS，支持基于调用关系的限流</td>
<td align="left">有限的支持</td>
</tr>
<tr>
<td align="left">流量整形</td>
<td align="left">支持慢启动、匀速器模式</td>
<td align="left">不支持</td>
</tr>
<tr>
<td align="left">系统负载保护</td>
<td align="left">支持</td>
<td align="left">不支持</td>
</tr>
<tr>
<td align="left">控制台</td>
<td align="left">开箱即用，可配置规则、查看秒级监控、机器发现等</td>
<td align="left">不完善</td>
</tr>
<tr>
<td align="left">常见框架的适配</td>
<td align="left">Servlet、Spring Cloud、Dubbo、gRPC 等</td>
<td align="left">Servlet、Spring Cloud Netflix</td>
</tr>
</tbody>
</table>
<p>Sentinel 于 2018 年 7 月份开源，截至本文写作之日已有 13k 的 Star，而 Hystrix 已经停止开发。Hystrix 不再维护可能也是 Sentinel 能快速进入大家眼球的原因之一。Hystrix 虽然不再维护，但依然开源，且 Hystrix 已经很稳定，不会因为不维护就不可用，只是不会再有更新。相比 Hystrix，Sentinel 更易于上手，Sentinel 是国内开源的项目，官方有提供中文文档，因此对只会中文的开发者较为友好，并且文档介绍得也很全面。</p>
<p>Hystrix 最核心的一项功能就是资源隔离，支持线程池隔离和信号量隔离。Sentinel 不支持线程池隔离，但使用 Sentinel 也可通过控制并发线程数方式提供信号量隔离。例如，控制服务 A 同时只能有 5 个线程去调用服务 B 的某个接口，或者控制服务 B 同时只能有 5 个线程去处理服务 A 发起调用的某个接口，避免因为一个接口消耗全部线程资源，导致服务奔溃。Hystrix 的线程池隔离可以为每个资源配置单独的线程池用于发送请求，但资源多的情况下会导致线程池增多，线程池增多会导致线程数增多，上下文切换会有非常大的损耗，对低延时的调用影响较大，因此 Hystrix 的线程池隔离也并未体现出多大的优势。</p>
<p>Sentinel 与 Hystrix 都支持基于失败比率的熔断降级，在调用超过指定的数量并且失败比率达到设定的阈值时触发熔断，并在下个时间窗口自动恢复。Sentinel 也支持按失败总数熔断降级，但按失败总数的熔断降级固定时间窗口为 1 分钟，当 1 分钟内调用失败总数达到设定的阈值就会触发熔断。除此之外，Sentinel 还支持基于平均响应时间的熔断降级，平均响应时间越长，说明服务的性能在持续下降，在响应时间持续飙高时自动熔断，可以防止调用慢造成级联阻塞。</p>
<p>Sentinel 和旧版本 Hystrix 的实时指标数据统计实现都是基于滑动窗口，指标数据统计指的是统计每个资源的当前窗口时间内的请求总数、处理成功总数、失败总数、总耗时、平均耗时、最大耗时、最小耗时、被降级总数等。使用滑动窗口可以循环利用一个数组，不需要重新申请内存，也不需要去删除过期的统计数据，降低 GC 的压力。Hystrix 1.5 版本对实时指标统计的实现进行了重构，将指标统计数据结构抽象成响应式流（reactive stream）的形式，方便消费者去利用指标信息，同时底层改造成基于 RxJava 的事件驱动模式，在服务调用成功、失败或超时时发布事件，通过一系列的变换和聚合最终得到实时的指标统计数据流，可以被熔断器或 Dashboard 消费 [1]。Sentinel 官方表示，未来将支持响应式流。</p>
<p>Sentinel 提供数据源接口可实现动态加载规则配置，结合 loadRules API 可灵活的运行时修改规则配置，并且随时修改随时生效。动态修改不仅支持修改某资源的规则配置，也支持添加新的资源规则配置或者移除资源规则配置。Sentinel 支持给同一个资源同时添加多种规则配置，当对同一个资源配置多种规则时，哪个规则先达到阈值就会触发哪个规则的降级。Hystrix 的资源模型设计上采用了命令模式，在创建 Command 时就需要指定隔离策略是线程池隔离还是信号量隔离，一但指定了隔离策略，运行期间便不能修改隔离策略，而在 Sentinel 中资源定义和规则配置是分离的，因此在配置的灵活性上 Sentinel 更具有优势。</p>
<p>Sentinel 支持系统自适应限流，Hystrix 所不支持的。当系统负载较高的时候，如果仍持续让请求进入，可能会导致系统崩溃，无法响应。在集群环境下，负载均衡把本应这台机器承载的流量转发到其它的机器上去，如果这个时候其它的机器也处在一个边缘状态的时候，这个增加的流量就会导致这台机器崩溃，最后导致整个集群不可用。针对这个情况，Sentinel 提供了对应的保护机制，让系统的入口流量和系统的负载达到一个平衡，保证系统在能力范围之内处理最多的请求 [2]。</p>
<p>在 QPS 过高的情况下，直接拒绝超出限制的请求是最常见的实现方式，但有些场景我们可能并不想直接拒绝请求，而是让请求排队等待处理，例如某一秒突增请求过多，但下一秒可能又没有请求或者请求很少的情况。Sentinel 的流量控制支持多种模式，例如直接拒绝模式、慢启动预热模式、匀速器模式。而慢启动预热模式和匀速器模式也是 Hystrix 所不支持的。</p>
<p>Sentinel 在框架的设计上使用了责任链模式和 SPI 机制提供扩展功能。使用 SPI 机制为 Sentinel 提供了更好的扩展性，例如，使用 SPI 支持自定义调用链构建器，使用自定义调用链构建器可实现按需选配降级功能（ProcessorSlot），并且还可以自己添加自定义降级功能（ProcessorSlot）。简单说，我们可以实现自定义降级功能，或者根据需要选择 Sentinel 提供的降级功能，移除不需要的，尽量降低 Sentinel 对服务的性能影响。</p>
<p>Sentinel 还支持集群限流。除了轮询负载均衡算法外，其它的算法都会导致流量到集群的每个节点都不一样，有的多有的少，假设服务 B 部署两个节点，对每个节点配置限流阈值为 200 QPS，我们希望集群的整体限量阈值是 400 QPS，但实际情况可能 400 个请求有 300 个请求分配到节点 1，只有 100 个请求分配到节点 2，导致总量没有到的情况下节点 1 就开始限流，因此单机维度限流会无法精确地限制总体流量。</p>
<p>集群流控可以精确地控制整个集群的调用总量，结合单机限流兜底，可以更好地发挥流量控制的效果。但实现集群限量需要一个 Server 专门统计集群的总调用量，其它的实例都要与 Server 通信来判断是否可以调用，也意味着每个请求都要增加一次额外的与 Server 通信的消耗，不过在使用单一长连接且 Server 处理“判断是否能通过”的耗时非常低，这个消耗对性能的影响还是可以接受的。</p>
<p>另外，黑白名单限流和热点参数限流也是 Sentinel 的一大特色。</p>
<p>黑白名单限流，可根据请求来源判断来源是否在黑名单中，如果在黑名单中则拒绝请求，否则放行，结合 Sentinel 的灵活动态配置，黑白名单可用于高峰期间对某些服务限流。</p>
<p>热点参数限流，统计调用 SphU.entry 传入参数中的热点参数，根据配置的限流阈值对包含热点参数的资源调用进行限流。热点参数限流仅对包含热点参数的资源调用生效，Sentinel 利用 LRU 策略统计最近最常访问的热点参数，结合令牌桶算法进行参数级别的流控，并且支持匀速流控效果。例如，想对某个热卖的商品限流，可将商品的 ID 为参数，统计一段时间内访问量最多的商品并进行限制。</p>
<p>Sentinel 提供的多种限流功能基本满足我们的所有需求，并且提供切入点让使用者可扩展 Sentinel 的功能，加上灵活的规则配置，以及 Sentinel 在性能上所作出的努力，都是 Sentinel 被广泛使用的原因。Sentinel 有阿里巴巴做信用背书，也在不断的优化、不断更新，相信 Sentinel 能做得更好。</p>
<h3>参考文献</h3>
<ul>
<li>[1]：<a href="https://github.com/alibaba/Sentinel/wiki/Sentinel-与-Hystrix-的对比">https://github.com/alibaba/Sentinel/wiki/Sentinel-与-Hystrix-的对比</a></li>
<li>[2]：<a href="https://github.com/alibaba/Sentinel/wiki">https://github.com/alibaba/Sentinel/wiki</a></li>
<li>[3]：<a href="https://mp.weixin.qq.com/s/12mjY9KawMoyc_DjC883uQ">https://mp.weixin.qq.com/s/12mjY9KawMoyc_DjC883uQ</a></li>
<li>[4]：<a href="https://www.jianshu.com/p/fcbc5de24153">https://www.jianshu.com/p/fcbc5de24153</a></li>
</ul>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="02&#32;为什么需要服务降级以及常见的几种降级方式.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="04&#32;Sentinel&#32;基于滑动窗口的实时指标数据统计.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435925ed1c645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
