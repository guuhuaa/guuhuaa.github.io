<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>18  知识点串讲：基于DDD的微服务设计实例.md</title>
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

                    
                    <a href="00&#32;开篇词&#32;&#32;学好了DDD，你能做什么？.md">00 开篇词  学好了DDD，你能做什么？.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;领域驱动设计：微服务设计为什么要选择DDD.md">01 领域驱动设计：微服务设计为什么要选择DDD.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;领域、子域、核心域、通用域和支撑域：傻傻分不清？.md">02 领域、子域、核心域、通用域和支撑域：傻傻分不清？.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;限界上下文：定义领域边界的利器">03 限界上下文：定义领域边界的利器</a>

                </li>
                <li>

                    
                    <a href="04&#32;实体和值对象：从领域模型的基础单元看系统设计.md">04 实体和值对象：从领域模型的基础单元看系统设计.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;聚合和聚合根：怎样设计聚合？.md">05  聚合和聚合根：怎样设计聚合？.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;领域事件：解耦微服务的关键.md">06  领域事件：解耦微服务的关键.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;DDD分层架构：有效降低层与层之间的依赖.md">07  DDD分层架构：有效降低层与层之间的依赖.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;微服务架构模型：几种常见模型的对比和分析.md">08  微服务架构模型：几种常见模型的对比和分析.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;中台：数字转型后到底应该共享什么？.md">09  中台：数字转型后到底应该共享什么？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;DDD、中台和微服务：它们是如何协作的？.md">10  DDD、中台和微服务：它们是如何协作的？.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;DDD实践：如何用DDD重构中台业务模型？.md">11  DDD实践：如何用DDD重构中台业务模型？.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;领域建模：如何用事件风暴构建领域模型？.md">12  领域建模：如何用事件风暴构建领域模型？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;代码模型（上）：如何使用DDD设计微服务代码模型？.md">13  代码模型（上）：如何使用DDD设计微服务代码模型？.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;代码模型（下）：如何保证领域模型与代码模型的一致性？.md">14  代码模型（下）：如何保证领域模型与代码模型的一致性？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;边界：微服务的各种边界在架构演进中的作用？.md">15  边界：微服务的各种边界在架构演进中的作用？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;视图：如何实现服务和数据在微服务各层的协作？.md">16  视图：如何实现服务和数据在微服务各层的协作？.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;从后端到前端：微服务后，前端如何设计？.md">17  从后端到前端：微服务后，前端如何设计？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="18&#32;&#32;知识点串讲：基于DDD的微服务设计实例.md">18  知识点串讲：基于DDD的微服务设计实例.md</a>
                    

                </li>
                <li>

                    
                    <a href="19&#32;&#32;总结（一）：微服务设计和拆分要坚持哪些原则？.md">19  总结（一）：微服务设计和拆分要坚持哪些原则？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;总结（二）：分布式架构关键设计10问.md">20  总结（二）：分布式架构关键设计10问.md</a>

                </li>
                <li>

                    
                    <a href="答疑：有关3个典型问题的讲解.md">答疑：有关3个典型问题的讲解.md</a>

                </li>
                <li>

                    
                    <a href="结束语&#32;&#32;所谓高手，就是跨过坑和大海.md">结束语  所谓高手，就是跨过坑和大海.md</a>

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
                        <div><h1>18  知识点串讲：基于DDD的微服务设计实例</h1>
<p>你好，我是欧创新。</p>
<p>为了更好地理解 DDD 的设计流程，今天我会用一个项目来带你了解 DDD 的战略设计和战术设计，走一遍从领域建模到微服务设计的全过程，一起掌握 DDD 的主要设计流程和关键点。</p>
<h2>项目基本信息</h2>
<p>项目的目标是实现在线请假和考勤管理。功能描述如下：</p>
<p>请假人填写请假单提交审批，根据请假人身份、请假类型和请假天数进行校验，根据审批规则逐级递交上级审批，逐级核批通过则完成审批，否则审批不通过退回申请人。</p>
<p>根据考勤规则，核销请假数据后，对考勤数据进行校验，输出考勤统计。</p>
<h2>战略设计</h2>
<p>战略设计是根据用户旅程分析，找出领域对象和聚合根，对实体和值对象进行聚类组成聚合，划分限界上下文，建立领域模型的过程。</p>
<p>战略设计采用的方法是事件风暴，包括：产品愿景、场景分析、领域建模和微服务拆分等几个主要过程。</p>
<p>战略设计阶段建议参与人员：领域专家、业务需求方、产品经理、架构师、项目经理、开发经理和测试经理。</p>
<h3>1. 产品愿景</h3>
<p>产品愿景是对产品顶层价值设计，对产品目标用户、核心价值、差异化竞争点等信息达成一致，避免产品偏离方向。</p>
<p>事件风暴时，所有参与者针对每一个要点，在贴纸上写出自己的意见，贴到白板上。事件风暴主持者会对每个贴纸，讨论并对发散的意见进行收敛和统一，形成下面的产品愿景图。</p>
<p><img src="assets/ef218e23ea2a8dc756af885ae06e61b2.jpg" alt="img" /></p>
<p>**我们把这个产品愿景图整理成一段文字就是：**为了满足内外部人员，他们的在线请假、自动考勤统计和外部人员管理的需求，我们建设这个在线请假考勤系统，它是一个在线请假平台，可以自动考勤统计。它可以同时支持内外网请假，同时管理内外部人员请假和定期考勤分析，而不像 HR 系统，只管理内部人员，且只能内网使用。我们的产品内外网皆可使用，可实现内外部人员无差异管理。</p>
<p>通过产品愿景分析，项目团队统一了系统名称——在线请假考勤系统，明确了项目目标和关键功能，与竞品（HR）的关键差异以及自己的优势和核心竞争力等。</p>
<p>产品愿景分析对于初创系统明确系统建设重点，统一团队建设目标和建立通用语言是很有价值的。但如果你的系统目标和需求非常清晰，这一步可以忽略。</p>
<h3>2. 场景分析</h3>
<p>场景分析是从用户视角出发，探索业务领域中的典型场景，产出领域中需要支撑的场景分类、用例操作以及不同子域之间的依赖关系，用以支撑领域建模。</p>
<p>项目团队成员一起用事件风暴分析请假和考勤的用户旅程。根据不同角色的旅程和场景分析，尽可能全面地梳理从前端操作到后端业务逻辑发生的所有操作、命令、领域事件以及外部依赖关系等信息。</p>
<p><strong>下面我就以请假和人员两个场景作为示例。</strong></p>
<p>第一个场景：请假</p>
<p>用户：请假人</p>
<p>请假人登录系统：从权限微服务获取请假人信息和权限数据，完成登录认证。</p>
<p>创建请假单：打开请假页面，选择请假类型和起始时间，录入请假信息。保存并创建请假单，提交请假审批。</p>
<p>修改请假单：查询请假单，打开请假页面，修改请假单，提交请假审批。</p>
<p>提交审批：获取审批规则，根据审批规则，从人员组织关系中获取审批人，给请假单分配审批人。</p>
<p>第二个场景：审批</p>
<p>用户：审批人</p>
<p>审批人登录系统：从权限微服务获取审批人信息和权限数据，完成登录认证。</p>
<p>获取请假单：获取审批人名下请假单，选择请假单。</p>
<p>审批：填写审批意见。</p>
<p>逐级审批：如果还需要上级审批，根据审批规则，从人员组织关系中获取审批人，给请假单分配审批人。重复以上 4 步。</p>
<p>最后审批人完成审批。</p>
<p>完成审批后，产生请假审批已通过领域事件。后续有两个进一步的业务操作：发送请假审批已通过的通知，通知邮件系统告知请假人；将请假数据发送到考勤以便核销。</p>
<p><img src="assets/33cbdd0f30a400a0cb9a2bd7ca5d54c5.jpg" alt="img" /></p>
<p>下面这个图是人员组织关系场景分析结果图，详细的分析过程以及考勤的场景分析就不描述了。</p>
<p><img src="assets/18acc5f5681c61a37957e5036f176274.jpg" alt="img" /></p>
<h3>3. 领域建模</h3>
<p>领域建模是通过对业务和问题域进行分析，建立领域模型。向上通过限界上下文指导微服务边界设计，向下通过聚合指导实体对象设计。</p>
<p>领域建模是一个收敛的过程，分三步：</p>
<p>第一步找出领域实体和值对象等领域对象；</p>
<p>第二步找出聚合根，根据实体、值对象与聚合根的依赖关系，建立聚合；</p>
<p>第三步根据业务及语义边界等因素，定义限界上下文。</p>
<p>下面我们就逐步详细讲解一下。</p>
<p><strong>第一步：找出实体和值对象等领域对象</strong></p>
<p>根据场景分析，分析并找出发起或产生这些命令或领域事件的实体和值对象。将与实体或值对象有关的命令和事件聚集到实体。</p>
<p>下面这个图是分析后的实体与命令的关系。通过分析，我们找到了：请假单、审批意见、审批规则、人员、组织关系、刷卡明细、考勤明细以及考勤统计等实体和值对象。</p>
<p><img src="assets/97c049d18f7e7032f6feef70992a4828.jpg" alt="img" /></p>
<p><strong>第二步：定义聚合</strong></p>
<p>定义聚合前，先找出聚合根。从上面的实体中，我们可以找出“请假单”和“人员”两个聚合根。然后找出与聚合根紧密依赖的实体和值对象。我们发现审批意见、审批规则和请假单紧密关联，组织关系和人员紧密关联。</p>
<p>找出这些实体的关系后，我们发现还有刷卡明细、考勤明细和考勤统计，这几个实体没有聚合根。这种情形在领域建模时你会经常遇到，对于这类场景我们需要分情况特殊处理。</p>
<p>刷卡明细、考勤明细和考勤统计这几个实体，它们之间相互独立，找不出聚合根，不是富领域模型，但它们一起完成考勤业务逻辑，具有很高的业务内聚性。我们将这几个业务关联紧密的实体，放在一个考勤聚合内。在微服务设计时，我们依然采用 DDD 的设计和分析方法。由于没有聚合根来管理聚合内的实体，我们可以用传统的方法来管理实体。</p>
<p>经过分析，我们建立了请假、人员组织关系和考勤三个聚合。其中请假聚合有请假单、审批意见实体和审批规则等值对象。人员组织关系聚合有人员和组织关系等实体。考勤聚合有刷卡明细、考勤明细和考勤统计等实体。</p>
<p><img src="assets/bb9f2a7095da0c72504e0195dca34376.jpg" alt="img" /></p>
<p><strong>第三步：定义限界上下文</strong></p>
<p>由于人员组织关系聚合与请假聚合，共同完成请假的业务功能，两者在请假的限界上下文内。考勤聚合则单独构成考勤统计限界上下文。因此我们为业务划分请假和考勤统计两个限界上下文，建立请假和考勤两个领域模型。</p>
<h3>4. 微服务的拆分</h3>
<p>理论上一个限界上下文就可以设计为一个微服务，但还需要综合考虑多种外部因素，比如：职责单一性、敏态与稳态业务分离、非功能性需求（如弹性伸缩、版本发布频率和安全等要求）、软件包大小、团队沟通效率和技术异构等非业务要素。</p>
<p>在这个项目，我们划分微服务主要考虑职责单一性原则。因此根据限界上下文就可以拆分为请假和考勤两个微服务。其中请假微服务包含人员组织关系和请假两个聚合，考勤微服务包含考勤聚合。</p>
<p>到这里，战略设计就结束了。通过战略设计，我们建立了领域模型，划分了微服务边界。下一步就是战术设计了，也就是微服务设计。下面我们以请假微服务为例，讲解其设计过程。</p>
<h2>战术设计</h2>
<p>战术设计是根据领域模型进行微服务设计的过程。这个阶段主要梳理微服务内的领域对象，梳理领域对象之间的关系，确定它们在代码模型和分层架构中的位置，建立领域模型与微服务模型的映射关系，以及服务之间的依赖关系。</p>
<p>战术设计阶段建议参与人员：领域专家、产品经理、架构师、项目经理、开发经理和测试经理等。</p>
<p>战术设计包括以下两个阶段：分析微服务领域对象和设计微服务代码结构。</p>
<h3>1. 分析微服务领域对象</h3>
<p>领域模型有很多领域对象，但是这些对象带有比较重的业务属性。要完成从领域模型到微服务的落地，还需要进一步的分析和设计。在事件风暴基础上，我们进一步细化领域对象以及它们的关系，补充事件风暴可能遗漏的业务和技术细节。</p>
<p>我们分析微服务内应该有哪些服务？服务的分层？应用服务由哪些服务组合和编排完成？领域服务包括哪些实体和实体方法？哪个实体是聚合根？实体有哪些属性和方法？哪些对象应该设计为值对象等。</p>
<p><strong>服务的识别和设计</strong></p>
<p>事件风暴的命令是外部的一些操作和业务行为，也是微服务对外提供的能力。它往往与微服务的应用服务或者领域服务对应。我们可以将命令作为服务识别和设计的起点。具体步骤如下：</p>
<p>根据命令设计应用服务，确定应用服务的功能，服务集合，组合和编排方式。服务集合中的服务包括领域服务或其它微服务的应用服务。</p>
<p>根据应用服务功能要求设计领域服务，定义领域服务。这里需要注意：应用服务可能是由多个聚合的领域服务组合而成的。</p>
<p>根据领域服务的功能，确定领域服务内的实体以及功能。</p>
<p>设计实体基本属性和方法。</p>
<p>另外，我们还要考虑领域事件的异步化处理。</p>
<p>我以提交审批这个动作为例，来说明服务的识别和设计。提交审批的大体流程是：</p>
<p>根据请假类型和时长，查询请假审批规则，获取下一步审批人的角色。</p>
<p>根据审批角色从人员组织关系中查询下一审批人。</p>
<p>为请假单分配审批人，并将审批规则保存至请假单。</p>
<p>通过分析，我们需要在应用层和领域层设计以下服务和方法。</p>
<p>**应用层：**提交审批应用服务。</p>
<p>**领域层：**领域服务有查询审批规则、修改请假流程信息服务以及根据审批规则查询审批人服务，分别位于请假和人员组织关系聚合。请假单实体有修改请假流程信息方法，审批规则值对象有查询审批规则方法。人员实体有根据审批规则查询审批人方法。下图是我们分析出来的服务以及它们之间的依赖关系。</p>
<p><img src="assets/eca31d653a3171a8272c6b1f25140bf7.png" alt="img" /></p>
<p>服务的识别和设计过程就是这样了，我们再来设计一下聚合内的对象。</p>
<p><strong>聚合中的对象</strong></p>
<p>在请假单聚合中，聚合根是请假单。</p>
<p>请假单经多级审核后，会产生多条审批意见，为了方便查询，我们可以将审批意见设计为实体。请假审批通过后，会产生请假审批通过的领域事件，因此还会有请假事件实体。请假聚合有以下实体：审批意见（记录审批人、审批状态和审批意见）和请假事件实体。</p>
<p>我们再来分析一下请假单聚合的值对象。请假人和下一审批人数据来源于人员组织关系聚合中的人员实体，可设计为值对象。人员类型、请假类型和审批状态是枚举值类型，可设计为值对象。确定请假审批规则后，审批规则也可作为请假单的值对象。请假单聚合将包含以下值对象：请假人、人员类型、请假类型、下一审批人、审批状态和审批规则。</p>
<p>综上，我们就可以画出请假聚合对象关系图了。</p>
<p><img src="assets/af21beade34a5f121f673c25a7c979be.jpg" alt="img" /></p>
<p>在人员组织关系聚合中，我们可以建立人员之间的组织关系，通过组织关系类型找到上级审批领导。它的聚合根是人员。实体有组织关系（包括组织关系类型和上级审批领导）。其中组织关系类型（如项目经理、处长、总经理等）是值对象。上级审批领导来源于人员聚合根，可设计为值对象。人员组织关系聚合将包含以下值对象：组织关系类型、上级审批领导。</p>
<p>综上，我们又可以画出人员组织关系聚合对象关系图了。</p>
<p><img src="assets/b56e20cd47d161eccbd86d014f9c6e76.jpg" alt="img" /></p>
<p><strong>微服务内的对象清单</strong></p>
<p>在确定各领域对象的属性后，我们就可以设计各领域对象在代码模型中的代码对象（包括代码对象的包名、类名和方法名），建立领域对象与代码对象的一一映射关系了。根据这种映射关系，相关人员可快速定位到业务逻辑所在的代码位置。在经过以上分析后，我们在微服务内就可以分析出如下图的对象清单。</p>
<p><img src="assets/89a65daccac054e97591c7259a60e4bc.jpg" alt="img" /></p>
<h3>2. 设计微服务代码结构</h3>
<p>根据 DDD 的代码模型和各领域对象所在的包、类和方法，我们可以定义出请假微服务的代码结构，设计代码对象。</p>
<p><strong>应用层代码结构</strong></p>
<p>应用层包括：应用服务、DTO 以及事件发布相关代码。在 LeaveApplicationService 类内实现与聚合相关的应用服务，在 LoginApplicationService 封装外部微服务认证和权限的应用服务。</p>
<p>这里提醒一下：如果应用服务逻辑复杂的话，一个应用服务就可以构建一个类，这样可以避免一个类的代码过于庞大，不利于维护。</p>
<p><img src="assets/ed9da0faabb9c756a0067dbd3f75d103.png" alt="img" /></p>
<p><strong>领域层代码结构</strong></p>
<p>领域层包括一个或多个聚合的实体类、事件实体类、领域服务以及工厂、仓储相关代码。一个聚合对应一个聚合代码目录，聚合之间在代码上完全隔离，聚合之间通过应用层协调。</p>
<p>请假微服务领域层包含请假和人员两个聚合。人员和请假代码都放在各自的聚合所在目录结构的代码包中。如果随着业务发展，人员相关功能需要从请假微服务中拆分出来，我们只需将人员聚合代码包稍加改造，独立部署，即可快速发布为人员微服务。到这里，微服务内的领域对象，分层以及依赖关系就梳理清晰了。微服务的总体架构和代码模型也基本搭建完成了。</p>
<p><img src="assets/a7fa9314002372f6ddad1c1b54573a66.png" alt="img" /></p>
<h2>后续的工作</h2>
<h3>1. 详细设计</h3>
<p>在完成领域模型和微服务设计后，我们还需要对微服务进行详细的设计。主要设计以下内容：实体属性、数据库表和字段、实体与数据库表映射、服务参数规约及功能实现等。</p>
<h3>2. 代码开发和测试</h3>
<p>开发人员只需要按照详细的设计文档和功能要求，找到业务功能对应的代码位置，完成代码开发就可以了。代码开发完成后，开发人员要编写单元测试用例，基于挡板模拟依赖对象完成服务测试。</p>
<h2>总结</h2>
<p>今天我们通过在线请假考勤项目，把 DDD 设计过程完整地走了一遍。</p>
<p>DDD 战略设计从事件风暴开始，然后我们要找出实体等领域对象，找出聚合根构建聚合，划分限界上下文，建立领域模型。</p>
<p>战术设计从事件风暴的命令开始，识别和设计服务，建立各层服务的依赖关系，设计微服务内的实体和值对象，找出微服务中所有的领域对象，并建立领域对象与代码对象的映射关系。</p>
<p>这样就可以很好地指导项目团队进行微服务开发和测试了。总结完毕，到这你是否已经清楚 DDD 全部的设计过程了呢？有疑问欢迎留言讨论。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="17&#32;&#32;从后端到前端：微服务后，前端如何设计？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="19&#32;&#32;总结（一）：微服务设计和拆分要坚持哪些原则？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433eb7c8cd70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/DDD%E5%AE%9E%E6%88%98%E8%AF%BE/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
