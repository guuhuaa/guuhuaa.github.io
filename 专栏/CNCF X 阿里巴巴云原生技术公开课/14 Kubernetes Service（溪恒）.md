<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>14 Kubernetes Service（溪恒）.md</title>
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

                    
                    <a href="13&#32;Kubernetes&#32;网络概念及策略控制（叶磊）.md">13 Kubernetes 网络概念及策略控制（叶磊）.md</a>

                </li>
                <li>

                    <a class="current-tab" href="14&#32;Kubernetes&#32;Service（溪恒）.md">14 Kubernetes Service（溪恒）.md</a>
                    

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
                        <div><h1>14 Kubernetes Service（溪恒）</h1>
<h2>需求来源</h2>
<h3>为什么需要服务发现</h3>
<p>在 K8s 集群里面会通过 pod 去部署应用，与传统的应用部署不同，传统应用部署在给定的机器上面去部署，我们知道怎么去调用别的机器的 IP 地址。但是在 K8s 集群里面应用是通过 pod 去部署的， 而 pod 生命周期是短暂的。在 pod 的生命周期过程中，比如它创建或销毁，它的 IP 地址都会发生变化，这样就不能使用传统的部署方式，不能指定 IP 去访问指定的应用。</p>
<p>另外在 K8s 的应用部署里，之前虽然学习了 deployment 的应用部署模式，但还是需要创建一个 pod 组，然后这些 pod 组需要提供一个统一的访问入口，以及怎么去控制流量负载均衡到这个组里面。比如说测试环境、预发环境和线上环境，其实在部署的过程中需要保持同样的一个部署模板以及访问方式。因为这样就可以用同一套应用的模板在不同的环境中直接发布。</p>
<h3>Service：Kubernetes 中的服务返现与负载均衡</h3>
<p>最后应用服务需要暴露到外部去访问，需要提供给外部的用户去调用的。我们上节了解到 pod 的网络跟机器不是同一个段的网络，那怎么让 pod 网络暴露到去给外部访问呢？这时就需要服务发现。</p>
<p><img src="assets/FsNSc0DcnIAm90gDtlBd-ipYG4aE" alt="avatar" /></p>
<p>在 K8s 里面，服务发现与负载均衡就是 K8s Service。上图就是在 K8s 里 Service 的架构，K8s Service 向上提供了外部网络以及 pod 网络的访问，即外部网络可以通过 service 去访问，pod 网络也可以通过 K8s Service 去访问。</p>
<p>向下，K8s 对接了另外一组 pod，即可以通过 K8s Service 的方式去负载均衡到一组 pod 上面去，这样相当于解决了前面所说的复发性问题，或者提供了统一的访问入口去做服务发现，然后又可以给外部网络访问，解决不同的 pod 之间的访问，提供统一的访问地址。</p>
<h2>用例解读</h2>
<p>下面进行实际的一个用例解读，看 pod K8s 的 service 要怎么去声明、怎么去使用？</p>
<h3>Service 语法</h3>
<p><img src="assets/Fl_9VxVULnLmtkexITpiECoDO-v1" alt="avatar" /></p>
<p>首先来看 K8s Service 的一个语法，上图实际就是 K8s 的一个声明结构。这个结构里有很多语法，跟之前所介绍的 K8s 的一些标准对象有很多相似之处。比如说标签 label 去做一些选择、selector 去做一些选择、label 去声明它的一些 label 标签等。</p>
<p>这里有一个新的知识点，就是定义了用于 K8s Service 服务发现的一个协议以及端口。继续来看这个模板，声明了一个名叫 my-service 的一个 K8s Service，它有一个 app:my-service 的 label，它选择了 app:MyApp 这样一个 label 的 pod 作为它的后端。</p>
<p>最后是定义的服务发现的协议以及端口，这个示例中我们定义的是 TCP 协议，端口是 80，目的端口是 9376，效果是访问到这个 service 80 端口会被路由到后端的 targetPort，就是只要访问到这个 service 80 端口的都会负载均衡到后端 app：MyApp 这种 label 的 pod 的 9376 端口。</p>
<h3>创建和查看 Service</h3>
<p>如何去创建刚才声明的这个 service 对象，以及它创建之后是什么样的效果呢？通过简单的命令：</p>
<ul>
<li>kubectl apply -f service.yaml</li>
</ul>
<p>或者是</p>
<ul>
<li>kubectl created -f service.yaml</li>
</ul>
<p>上面的命令可以简单地去创建这样一个 service。创建好之后，可以通过：</p>
<ul>
<li>kubectl discribe service</li>
</ul>
<p>去查看 service 创建之后的一个结果。</p>
<p><img src="assets/FjSOqAh-KD96eHj5Cm1lwApCPArZ" alt="avatar" /></p>
<p>service 创建好之后，你可以看到它的名字是 my-service。Namespace、Label、Selector 这些都跟我们之前声明的一样，这里声明完之后会生成一个 IP 地址，这个 IP 地址就是 service 的 IP 地址，这个 IP 地址在集群里面可以被其它 pod 所访问，相当于通过这个 IP 地址提供了统一的一个 pod 的访问入口，以及服务发现。</p>
<p>这里还有一个 Endpoints 的属性，就是我们通过 Endpoints 可以看到：通过前面所声明的 selector 去选择了哪些 pod？以及这些 pod 都是什么样一个状态？比如说通过 selector，我们看到它选择了这些 pod 的一个 IP，以及这些 pod 所声明的 targetPort 的一个端口。</p>
<p><img src="assets/FtrSVn8y4xXkzK2W_ypZA-bg6KFX" alt="avatar" /></p>
<p>实际的架构如上图所示。在 service 创建之后，它会在集群里面创建一个虚拟的 IP 地址以及端口，在集群里，所有的 pod 和 node 都可以通过这样一个 IP 地址和端口去访问到这个 service。这个 service 会把它选择的 pod 及其 IP 地址都挂载到后端。这样通过 service 的 IP 地址访问时，就可以负载均衡到后端这些 pod 上面去。</p>
<p>当 pod 的生命周期有变化时，比如说其中一个 pod 销毁，service 就会自动从后端摘除这个 pod。这样实现了：就算 pod 的生命周期有变化，它访问的端点是不会发生变化的。</p>
<h3>集群内访问 Service</h3>
<p>在集群里面，其他 pod 要怎么访问到我们所创建的这个 service 呢？有三种方式：</p>
<ul>
<li>首先我们可以通过 service 的虚拟 IP 去访问，比如说刚创建的 my-service 这个服务，通过 kubectl get svc 或者 kubectl discribe service 都可以看到它的虚拟 IP 地址是 172.29.3.27，端口是 80，然后就可以通过这个虚拟 IP 及端口在 pod 里面直接访问到这个 service 的地址。</li>
<li>第二种方式直接访问服务名，依靠 DNS 解析，就是同一个 namespace 里 pod 可以直接通过 service 的名字去访问到刚才所声明的这个 service。不同的 namespace 里面，我们可以通过 service 名字加“.”，然后加 service 所在的哪个 namespace 去访问这个 service，例如我们直接用 curl 去访问，就是 my-service:80 就可以访问到这个 service。</li>
<li>第三种是通过环境变量访问，在同一个 namespace 里的 pod 启动时，K8s 会把 service 的一些 IP 地址、端口，以及一些简单的配置，通过环境变量的方式放到 K8s 的 pod 里面。在 K8s pod 的容器启动之后，通过读取系统的环境变量比读取到 namespace 里面其他 service 配置的一个地址，或者是它的端口号等等。比如在集群的某一个 pod 里面，可以直接通过 curl $ 取到一个环境变量的值，比如取到 MY<em>SERVICE</em>SERVICE<em>HOST 就是它的一个 IP 地址，MY</em>SERVICE 就是刚才我们声明的 MY<em>SERVICE，SERVICE</em>PORT 就是它的端口号，这样也可以请求到集群里面的 MY_SERVICE 这个 service。</li>
</ul>
<h3>Headless Service</h3>
<p>service 有一个特别的形态就是 Headless Service。service 创建的时候可以指定 clusterIP:None，告诉 K8s 说我不需要 clusterIP（就是刚才所说的集群里面的一个虚拟 IP），然后 K8s 就不会分配给这个 service 一个虚拟 IP 地址，它没有虚拟 IP 地址怎么做到负载均衡以及统一的访问入口呢？</p>
<p>它是这样来操作的：pod 可以直接通过 service_name 用 DNS 的方式解析到所有后端 pod 的 IP 地址，通过 DNS 的 A 记录的方式会解析到所有后端的 Pod 的地址，由客户端选择一个后端的 IP 地址，这个 A 记录会随着 pod 的生命周期变化，返回的 A 记录列表也发生变化，这样就要求客户端应用要从 A 记录把所有 DNS 返回到 A 记录的列表里面 IP 地址中，客户端自己去选择一个合适的地址去访问 pod。</p>
<p><img src="assets/FpaWBf0-QsUFdbAv_c76ZeZLSmuO" alt="avatar" /></p>
<p>可以从上图看一下跟刚才我们声明的模板的区别，就是在中间加了一个 clusterIP:None，即表明不需要虚拟 IP。实际效果就是集群的 pod 访问 my-service 时，会直接解析到所有的 service 对应 pod 的 IP 地址，返回给 pod，然后 pod 里面自己去选择一个 IP 地址去直接访问。</p>
<h3>向集群外暴露 Service</h3>
<p>前面介绍的都是在集群里面 node 或者 pod 去访问 service，service 怎么去向外暴露呢？怎么把应用实际暴露给公网去访问呢？这里 service 也有两种类型去解决这个问题，一个是 NodePort，一个是 LoadBalancer。</p>
<ul>
<li>
<p>NodePort 的方式就是在集群的 node 上面（即集群的节点的宿主机上面）去暴露节点上的一个端口，这样相当于在节点的一个端口上面访问到之后就会再去做一层转发，转发到虚拟的 IP 地址上面，就是刚刚宿主机上面 service 虚拟 IP 地址。</p>
</li>
<li>
<p>LoadBalancer 类型就是在 NodePort 上面又做了一层转换，刚才所说的 NodePort 其实是集群里面每个节点上面一个端口，LoadBalancer 是在所有的节点前又挂一个负载均衡。比如在阿里云上挂一个 SLB，这个负载均衡会提供一个统一的入口，并把所有它接触到的流量负载均衡到每一个集群节点的 node pod 上面去。然后 node pod 再转化成 ClusterIP，去访问到实际的 pod 上面。</p>
</li>
</ul>
<h2>操作演示</h2>
<p>下面进行实际操作演示，在阿里云的容器服务上面进去体验一下如何使用 K8s Service。</p>
<h3>创建 Service</h3>
<p>我们已经创建好了一个阿里云的容器集群，然后并且配置好本地终端到阿里云容器集群的一个连接。</p>
<p>首先可以通过 kubectl get cs ，可以看到我们已经正常连接到了阿里云容器服务的集群上面去。</p>
<p><img src="assets/FussFCyed8qkgeqLQQqlja_vG2ln" alt="avatar" /></p>
<p>今天将通过这些模板实际去体验阿里云服务上面去使用 K8s Service。有三个模板，首先是 client，就是用来模拟通过 service 去访问 K8s 的 service，然后负载均衡到我们的 service 里面去声明的一组 pod 上。</p>
<p><img src="assets/FlkYzXSj2LQOsZ3VP8noupeMgcno" alt="avatar" /></p>
<p>K8s Service 的上面，跟刚才介绍一样，我们创建了一个 K8s Service 模板，里面 pod，K8s Service 会通过前端指定的 80 端口负载均衡到后端 pod 的 80 端口上面，然后 selector 选择到 run:nginx 这样标签的一些 pod 去作为它的后端。</p>
<p><img src="assets/FoNi0Bx7CTNHvlsvoORGa7K6CitD" alt="avatar" /></p>
<p>然后去创建带有这样标签的一组 pod，通过什么去创建 pod 呢？就是之前所介绍的 K8s deployment，通过 deployment 我们可以轻松创建出一组 pod，然后上面声明 run:nginx 这样一个label，并且它有两个副本，会同时跑出来两个 pod。</p>
<p><img src="assets/Fo9OvQITzJLl-GmHd3_mcwImzs1q" alt="avatar" /></p>
<p>先创建一组 pod，就是创建这个 K8s deployment，通过 kubectl create -f service.yaml。这个 deployment 也创建好了，再看一下 pod 有没有创建出来。如下图看到这个 deployment 所创建的两个 pod 都已经在 running 了。通过 kubectl get pod -o wide 可以看到 IP 地址。通过 -l，即 label 去做筛选，run=nginx。如下图所示可以看到，这两个 pod 分别是 10.0.0.135 和 10.0.0.12 这样一个 IP 地址，并且都是带 run=nginx 这个 label 的。</p>
<p><img src="assets/FrO8OaFDt8TTk4TIIcKgrR2JQom5" alt="avatar" /></p>
<p>下面我们去创建 K8s service，就是刚才介绍的通过 service 去选择这两个 pod。这个 service 已经创建好了。</p>
<p><img src="assets/Fl1Remwwd4dM5XwQI-dipSmubSCC" alt="avatar" /></p>
<p>根据刚才介绍，通过 kubectl describe svc 可以看到这个 service 实际的一个状态。如下图所示，刚才创建的 nginx service，它的选择器是 run=nginx，通过 run=nginx 这个选择器选择到后端的 pod 地址，就是刚才所看到那两个 pod 的地址：10.0.0.12 和 10.0.0.135。这里可以看到 K8s 为它生成了集群里面一个虚拟 IP 地址，通过这个虚拟 IP 地址，它就可以负载均衡到后面的两个 pod 上面去。</p>
<p><img src="assets/FgIJa7up714MeuWzxs03RgCmzO9o" alt="avatar" /></p>
<p>现在去创建一个客户端的 pod 实际去感受一下如何去访问这个 K8s Service，我们通过 client.yaml 去创建客户端的 pod，kubectl get pod 可以看到客户端 pod 已经创建好并且已经在运行中了。</p>
<p><img src="assets/FolM0NWD4tOaeJpv94h2Y46NLR2U" alt="avatar" /></p>
<p>通过 kubectl exec 到这个 pod 里面，进入这个 pod 去感受一下刚才所说的三种访问方式，首先可以直接去访问这个 K8s 为它生成的这个 ClusterIP，就是虚拟 IP 地址，通过 curl 访问这个 IP 地址，这个 pod 里面没有装 curl。通过 wget 这个 IP 地址，输入进去测试一下。可以看到通过这个去访问到实际的 IP 地址是可以访问到后端的 nginx 上面的，这个虚拟是一个统一的入口。</p>
<p><img src="assets/FljsuZcLh2n6_0wvbhJkgQw0h1hs" alt="avatar" /></p>
<p>第二种方式，可以通过直接 service 名字的方式去访问到这个 service。同样通过 wget，访问我们刚才所创建的 service 名 nginx，可以发现跟刚才看到的结果是一样的。</p>
<p><img src="assets/Fi5yxWwlD_JIk5E55H88SN64StcH" alt="avatar" /></p>
<p>在不同的 namespace 时，也可以通过加上 namespace 的一个名字去访问到 service，比如这里的 namespace 为 default。 <img src="assets/Fq_yIQCrXUv5Y4m_vILXYKug7P5o" alt="avatar" /></p>
<p>最后我们介绍的访问方式里面还可以通过环境变量去访问，在这个 pod 里面直接通过执行 env 命令看一下它实际注入的环境变量的情况。看一下 nginx 的 service 的各种配置已经注册进来了。</p>
<p><img src="assets/FiEdQgHfGb6VXlLk-bcufkLyDjH_" alt="avatar" /></p>
<p>可以通过 wget 同样去访问这样一个环境变量，然后可以访问到我们的一个 service。</p>
<p><img src="assets/Fs4FQn_R-mqcrssjuNQfrLJUVS_V" alt="avatar" /></p>
<p>介绍完这三种访问方式，再看一下如何通过 service 外部的网络去访问。我们 vim 直接修改一些刚才所创建的 service。</p>
<p><img src="assets/FhyPM4xafUuVVzDvSXbnJfCHM8J4" alt="avatar" /></p>
<p>最后我们添加一个 type，就是 LoadBalancer，就是我们前面所介绍的外部访问的方式。</p>
<p><img src="assets/FkST3Et2rFn638rTbcVW1KGbwC90" alt="avatar" /></p>
<p>然后通过 kubectl apply，这样就把刚刚修改的内容直接生效在所创建的 service 里面。</p>
<p><img src="assets/Fqea8W8Ogt2-owgI6bXp5DXjgokt" alt="avatar" /></p>
<p>现在看一下 service 会有哪些变化呢？通过 kubectl get svc -o wide，我们发现刚刚创建的 nginx service 多了一个 EXTERNAL-IP，就是外部访问的一个 IP 地址，刚才我们所访问的都是 CLUSTER-IP，就是在集群里面的一个虚拟 IP 地址。</p>
<p><img src="assets/Fjbn-BHV2p-H30EvE7la_JAA9apy" alt="avatar" /></p>
<p>然后现在实际去访问一下这个外部 IP 地址 39.98.21.187，感受一下如何通过 service 去暴露我们的应用服务，直接在终端里面点一下，这里可以看到我们直接通过这个应用的外部访问端点，可以访问到这个 service，是不是很简单？</p>
<p><img src="assets/Fg_4hT2V3pLzFQv3DwoNJ-NV6PXU" alt="avatar" /></p>
<p>我们最后再看一下用 service 去实现了 K8s 的服务发现，就是 service 的访问地址跟 pod 的生命周期没有关系。我们先看一下现在的 service 后面选择的是这两个 pod IP 地址。</p>
<p><img src="assets/Fu5UojYcffLzszDkpSRYtLftgMKf" alt="avatar" /></p>
<p>我们现在把其中的一个 pod 删掉，通过 kubectl delete 的方式把前面一个 pod 删掉。</p>
<p><img src="assets/FotfekPF1eKhNRI3-PRJVo2eL5NC" alt="avatar" /></p>
<p>我们知道 deployment 会让它自动生成一个新的 pod，现在看 IP 地址已经变成 137。</p>
<p><img src="assets/FgZVDOs5m09juiP1Q9pWuN1Y0qoW" alt="avatar" /></p>
<p>现在再去 describe 一下刚才的 service，如下图,看到前面访问端点就是集群的 IP 地址没有发生变化，对外的 LoadBalancer 的 IP 地址也没有发生变化。在所有不影响客户端的访问情况下，后端的一个 pod IP 已经自动放到了 service 后端里面。</p>
<p><img src="assets/Frw3OFsRfAMCivcDWFfUKjnGWPJi" alt="avatar" /></p>
<p>这样就相当于在应用的组件调用的时候可以不用关心 pod 在生命周期的一个变化。</p>
<p>以上就是所有演示。</p>
<h2>架构设计</h2>
<p>** **最后是对 K8s 设计的一个简单的分析以及实现的一些原理。</p>
<h3>Kubernetes 服务发现架构</h3>
<p><img src="assets/FrLOYwy8Lgh8Rkeue3Gawhco_F0C" alt="avatar" /></p>
<p>如上图所示，K8s 服务发现以及 K8s Service 是这样整体的一个架构。</p>
<p>K8s 分为 master 节点和 worker 节点：</p>
<ul>
<li>master 里面主要是 K8s 管控的内容；</li>
<li>worker 节点里面是实际跑用户应用的一个地方。</li>
</ul>
<p>在 K8s master 节点里面有 APIServer，就是统一管理 K8s 所有对象的地方，所有的组件都会注册到 APIServer 上面去监听这个对象的变化，比如说我们刚才的组件 pod 生命周期发生变化，这些事件。</p>
<p>这里面最关键的有三个组件：</p>
<ul>
<li>一个是 Cloud Controller Manager，负责去配置 LoadBalancer 的一个负载均衡器给外部去访问；</li>
<li>另外一个就是 Coredns，就是通过 Coredns 去观测 APIServer 里面的 service 后端 pod 的一个变化，去配置 service 的 DNS 解析，实现可以通过 service 的名字直接访问到 service 的虚拟 IP，或者是 Headless 类型的 Service 中的 IP 列表的解析；</li>
<li>然后在每个 node 里面会有 kube-proxy 这个组件，它通过监听 service 以及 pod 变化，然后实际去配置集群里面的 node pod 或者是虚拟 IP 地址的一个访问。</li>
</ul>
<p>实际访问链路是什么样的呢？比如说从集群内部的一个 Client Pod3 去访问 Service，就类似于刚才所演示的一个效果。Client Pod3 首先通过 Coredns 这里去解析出 ServiceIP，Coredns 会返回给它 ServiceName 所对应的 service IP 是什么，这个 Client Pod3 就会拿这个 Service IP 去做请求，它的请求到宿主机的网络之后，就会被 kube-proxy 所配置的 iptables 或者 IPVS 去做一层拦截处理，之后去负载均衡到每一个实际的后端 pod 上面去，这样就实现了一个负载均衡以及服务发现。</p>
<p>对于外部的流量，比如说刚才通过公网访问的一个请求。它是通过外部的一个负载均衡器 Cloud Controller Manager 去监听 service 的变化之后，去配置的一个负载均衡器，然后转发到节点上的一个 NodePort 上面去，NodePort 也会经过 kube-proxy 的一个配置的一个 iptables，把 NodePort 的流量转换成 ClusterIP，紧接着转换成后端的一个 pod 的 IP 地址，去做负载均衡以及服务发现。这就是整个 K8s 服务发现以及 K8s Service 整体的结构。</p>
<h3>后续进阶</h3>
<p>后续再进阶部分我们还会更加深入地去讲解 K8s Service 的实现原理，以及在 service 网络出问题之后，如何去诊断以及去修复的技巧。</p>
<h2>本节总结</h2>
<p>本节课的主要内容就到此为止了，这里为大家简单总结一下：</p>
<ol>
<li>为什么云原生的场景需要服务发现和负载均衡，</li>
<li>在 Kubernetes 中如何使用 Kubernetes 的 Service 做服务发现和负载均衡</li>
<li>Kubernetes 集群中 Service 涉及到的组件和大概实现原理</li>
</ol>
<p>相信经过这一节的学习大家能够通过 Kubernetes Service 将复杂的企业级应用快速并标准的编排起来。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="13&#32;Kubernetes&#32;网络概念及策略控制（叶磊）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="15&#32;从&#32;0&#32;开始创作云原生应用（殷达）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433deb4ac970ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
