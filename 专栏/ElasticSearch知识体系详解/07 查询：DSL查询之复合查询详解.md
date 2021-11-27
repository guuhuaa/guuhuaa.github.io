<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>07 查询：DSL查询之复合查询详解.md</title>
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

                    
                    <a href="01&#32;认知：ElasticSearch基础概念.md">01 认知：ElasticSearch基础概念.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;认知：Elastic&#32;Stack生态和场景方案.md">02 认知：Elastic Stack生态和场景方案.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;安装：ElasticSearch和Kibana安装.md">03 安装：ElasticSearch和Kibana安装.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;入门：查询和聚合的基础使用.md">04 入门：查询和聚合的基础使用.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;索引：索引管理详解.md">05 索引：索引管理详解.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;索引：索引模板(Index&#32;Template)详解.md">06 索引：索引模板(Index Template)详解.md</a>

                </li>
                <li>

                    <a class="current-tab" href="07&#32;查询：DSL查询之复合查询详解.md">07 查询：DSL查询之复合查询详解.md</a>
                    

                </li>
                <li>

                    
                    <a href="08&#32;查询：DSL查询之全文搜索详解.md">08 查询：DSL查询之全文搜索详解.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;查询：DSL查询之Term详解.md">09 查询：DSL查询之Term详解.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;聚合：聚合查询之Bucket聚合详解.md">10 聚合：聚合查询之Bucket聚合详解.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;聚合：聚合查询之Metric聚合详解.md">11 聚合：聚合查询之Metric聚合详解.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;聚合：聚合查询之Pipline聚合详解.md">12 聚合：聚合查询之Pipline聚合详解.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;原理：从图解构筑对ES原理的初步认知.md">13 原理：从图解构筑对ES原理的初步认知.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;原理：ES原理知识点补充和整体结构.md">14 原理：ES原理知识点补充和整体结构.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;原理：ES原理之索引文档流程详解.md">15 原理：ES原理之索引文档流程详解.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;原理：ES原理之读取文档流程详解.md">16 原理：ES原理之读取文档流程详解.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;优化：ElasticSearch性能优化详解.md">17 优化：ElasticSearch性能优化详解.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;大厂实践：腾讯万亿级&#32;Elasticsearch&#32;技术实践.md">18 大厂实践：腾讯万亿级 Elasticsearch 技术实践.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;资料：Awesome&#32;Elasticsearch.md">19 资料：Awesome Elasticsearch.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;WrapperQuery.md">20 WrapperQuery.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;备份和迁移.md">21 备份和迁移.md</a>

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
                        <div><h1>07 查询：DSL查询之复合查询详解</h1>
<h2>复合查询引入</h2>
<p>在(前文-多条件查询-bool)中，我们使用<code>bool</code>查询来组合多个查询条件。</p>
<p>比如之前介绍的语句</p>
<pre><code class="language-bash">GET /bank/_search
{
  &quot;query&quot;: {
    &quot;bool&quot;: {
      &quot;must&quot;: [
        { &quot;match&quot;: { &quot;age&quot;: &quot;40&quot; } }
      ],
      &quot;must_not&quot;: [
        { &quot;match&quot;: { &quot;state&quot;: &quot;ID&quot; } }
      ]
    }
  }
}
</code></pre>
<p>这种查询就是本文要介绍的<strong>复合查询</strong>，并且bool查询只是复合查询一种。</p>
<h2>bool query(布尔查询)</h2>
<blockquote>
<p>通过布尔逻辑将较小的查询组合成较大的查询。</p>
</blockquote>
<h3>概念</h3>
<p>Bool查询语法有以下特点</p>
<ul>
<li>子查询可以任意顺序出现</li>
<li>可以嵌套多个查询，包括bool查询</li>
<li>如果bool查询中没有must条件，should中必须至少满足一条才会返回结果。</li>
</ul>
<p>bool查询包含四种操作符，分别是must,should,must_not,filter。他们均是一种数组，数组里面是对应的判断条件。</p>
<ul>
<li><code>must</code>： 必须匹配。贡献算分</li>
<li><code>must_not</code>：过滤子句，必须不能匹配，但不贡献算分</li>
<li><code>should</code>： 选择性匹配，至少满足一条。贡献算分</li>
<li><code>filter</code>： 过滤子句，必须匹配，但不贡献算分</li>
</ul>
<h3>一些例子</h3>
<p>看下官方举例</p>
<ul>
<li>例子1</li>
</ul>
<pre><code class="language-bash">POST _search
{
  &quot;query&quot;: {
    &quot;bool&quot; : {
      &quot;must&quot; : {
        &quot;term&quot; : { &quot;user.id&quot; : &quot;kimchy&quot; }
      },
      &quot;filter&quot;: {
        &quot;term&quot; : { &quot;tags&quot; : &quot;production&quot; }
      },
      &quot;must_not&quot; : {
        &quot;range&quot; : {
          &quot;age&quot; : { &quot;gte&quot; : 10, &quot;lte&quot; : 20 }
        }
      },
      &quot;should&quot; : [
        { &quot;term&quot; : { &quot;tags&quot; : &quot;env1&quot; } },
        { &quot;term&quot; : { &quot;tags&quot; : &quot;deployed&quot; } }
      ],
      &quot;minimum_should_match&quot; : 1,
      &quot;boost&quot; : 1.0
    }
  }
}
</code></pre>
<p>在filter元素下指定的查询对评分没有影响 , 评分返回为0。分数仅受已指定查询的影响。</p>
<ul>
<li>例子2</li>
</ul>
<pre><code class="language-bash">GET _search
{
  &quot;query&quot;: {
    &quot;bool&quot;: {
      &quot;filter&quot;: {
        &quot;term&quot;: {
          &quot;status&quot;: &quot;active&quot;
        }
      }
    }
  }
}
</code></pre>
<p>这个例子查询查询为所有文档分配0分，因为没有指定评分查询。</p>
<ul>
<li>例子3</li>
</ul>
<pre><code class="language-bash">GET _search
{
  &quot;query&quot;: {
    &quot;bool&quot;: {
      &quot;must&quot;: {
        &quot;match_all&quot;: {}
      },
      &quot;filter&quot;: {
        &quot;term&quot;: {
          &quot;status&quot;: &quot;active&quot;
        }
      }
    }
  }
}
</code></pre>
<p>此bool查询具有match_all查询，该查询为所有文档指定1.0分。</p>
<ul>
<li>例子4</li>
</ul>
<pre><code class="language-bash">GET /_search
{
  &quot;query&quot;: {
    &quot;bool&quot;: {
      &quot;should&quot;: [
        { &quot;match&quot;: { &quot;name.first&quot;: { &quot;query&quot;: &quot;shay&quot;, &quot;_name&quot;: &quot;first&quot; } } },
        { &quot;match&quot;: { &quot;name.last&quot;: { &quot;query&quot;: &quot;banon&quot;, &quot;_name&quot;: &quot;last&quot; } } }
      ],
      &quot;filter&quot;: {
        &quot;terms&quot;: {
          &quot;name.last&quot;: [ &quot;banon&quot;, &quot;kimchy&quot; ],
          &quot;_name&quot;: &quot;test&quot;
        }
      }
    }
  }
}
</code></pre>
<p>每个query条件都可以有一个<code>_name</code>属性，用来追踪搜索出的数据到底match了哪个条件。</p>
<h2>boosting query(提高查询)</h2>
<blockquote>
<p>不同于bool查询，bool查询中只要一个子查询条件不匹配那么搜索的数据就不会出现。而boosting query则是降低显示的权重/优先级（即score)。</p>
</blockquote>
<h3>概念</h3>
<p>比如搜索逻辑是 name = 'apple' and type ='fruit'，对于只满足部分条件的数据，不是不显示，而是降低显示的优先级（即score)</p>
<h3>例子</h3>
<p>首先创建数据</p>
<pre><code class="language-bash">POST /test-dsl-boosting/_bulk
{ &quot;index&quot;: { &quot;_id&quot;: 1 }}
{ &quot;content&quot;:&quot;Apple Mac&quot; }
{ &quot;index&quot;: { &quot;_id&quot;: 2 }}
{ &quot;content&quot;:&quot;Apple Fruit&quot; }
{ &quot;index&quot;: { &quot;_id&quot;: 3 }}
{ &quot;content&quot;:&quot;Apple employee like Apple Pie and Apple Juice&quot; }
</code></pre>
<p>对匹配<code>pie</code>的做降级显示处理</p>
<pre><code class="language-bash">GET /test-dsl-boosting/_search
{
  &quot;query&quot;: {
    &quot;boosting&quot;: {
      &quot;positive&quot;: {
        &quot;term&quot;: {
          &quot;content&quot;: &quot;apple&quot;
        }
      },
      &quot;negative&quot;: {
        &quot;term&quot;: {
          &quot;content&quot;: &quot;pie&quot;
        }
      },
      &quot;negative_boost&quot;: 0.5
    }
  }
}
</code></pre>
<p>执行结果如下</p>
<p><img src="assets/es-dsl-com-2.png" alt="img" /></p>
<h2>constant_score（固定分数查询）</h2>
<blockquote>
<p>查询某个条件时，固定的返回指定的score；显然当不需要计算score时，只需要filter条件即可，因为filter context忽略score。</p>
</blockquote>
<h3>例子</h3>
<p>首先创建数据</p>
<pre><code class="language-bash">POST /test-dsl-constant/_bulk
{ &quot;index&quot;: { &quot;_id&quot;: 1 }}
{ &quot;content&quot;:&quot;Apple Mac&quot; }
{ &quot;index&quot;: { &quot;_id&quot;: 2 }}
{ &quot;content&quot;:&quot;Apple Fruit&quot; }
</code></pre>
<p>查询apple</p>
<pre><code class="language-bash">GET /test-dsl-constant/_search
{
  &quot;query&quot;: {
    &quot;constant_score&quot;: {
      &quot;filter&quot;: {
        &quot;term&quot;: { &quot;content&quot;: &quot;apple&quot; }
      },
      &quot;boost&quot;: 1.2
    }
  }
}
</code></pre>
<p>执行结果如下</p>
<p><img src="assets/es-dsl-com-3.png" alt="img" /></p>
<h2>dis_max(最佳匹配查询）</h2>
<blockquote>
<p>分离最大化查询（Disjunction Max Query）指的是： 将任何与任一查询匹配的文档作为结果返回，但只将最佳匹配的评分作为查询的评分结果返回 。</p>
</blockquote>
<h3>例子</h3>
<p>假设有个网站允许用户搜索博客的内容，以下面两篇博客内容文档为例：</p>
<pre><code class="language-bash">POST /test-dsl-dis-max/_bulk
{ &quot;index&quot;: { &quot;_id&quot;: 1 }}
{&quot;title&quot;: &quot;Quick brown rabbits&quot;,&quot;body&quot;:  &quot;Brown rabbits are commonly seen.&quot;}
{ &quot;index&quot;: { &quot;_id&quot;: 2 }}
{&quot;title&quot;: &quot;Keeping pets healthy&quot;,&quot;body&quot;:  &quot;My quick brown fox eats rabbits on a regular basis.&quot;}
</code></pre>
<p>用户输入词组 “Brown fox” 然后点击搜索按钮。事先，我们并不知道用户的搜索项是会在 title 还是在 body 字段中被找到，但是，用户很有可能是想搜索相关的词组。用肉眼判断，文档 2 的匹配度更高，因为它同时包括要查找的两个词：</p>
<p>现在运行以下 bool 查询：</p>
<pre><code class="language-bash">GET /test-dsl-dis-max/_search
{
    &quot;query&quot;: {
        &quot;bool&quot;: {
            &quot;should&quot;: [
                { &quot;match&quot;: { &quot;title&quot;: &quot;Brown fox&quot; }},
                { &quot;match&quot;: { &quot;body&quot;:  &quot;Brown fox&quot; }}
            ]
        }
    }
}
</code></pre>
<p><img src="assets/es-dsl-dismax-2.png" alt="img" /></p>
<p>为了理解导致这样的原因，需要看下如何计算评分的</p>
<ul>
<li><strong>should 条件的计算分数</strong></li>
</ul>
<pre><code class="language-bash">GET /test-dsl-dis-max/_search
{
    &quot;query&quot;: {
        &quot;bool&quot;: {
            &quot;should&quot;: [
                { &quot;match&quot;: { &quot;title&quot;: &quot;Brown fox&quot; }},
                { &quot;match&quot;: { &quot;body&quot;:  &quot;Brown fox&quot; }}
            ]
        }
    }
}
</code></pre>
<p>要计算上述分数，首先要计算match的分数</p>
<ol>
<li>第一个match 中 <code>brown的分数</code></li>
</ol>
<p>doc 1 分数 = 0.6931471</p>
<p><img src="assets/es-dsl-dismax-4.png" alt="img" /></p>
<ol>
<li>title中没有fox，所以第一个match 中 <code>brown fox 的分数 = brown分数 + 0 = 0.6931471</code></li>
</ol>
<p>doc 1 分数 = 0.6931471 + 0 = 0.6931471</p>
<p><img src="assets/es-dsl-dismax-5.png" alt="img" /></p>
<ol>
<li>第二个 match 中 <code>brown分数</code></li>
</ol>
<p>doc 1 分数 = 0.21110919</p>
<p>doc 2 分数 = 0.160443</p>
<p><img src="assets/es-dsl-dismax-6.png" alt="img" /></p>
<ol>
<li>第二个 match 中 <code>fox分数</code></li>
</ol>
<p>doc 1 分数 = 0</p>
<p>doc 2 分数 = 0.60996956</p>
<p><img src="assets/es-dsl-dismax-7.png" alt="img" /></p>
<ol>
<li>所以第二个 match 中 <code>brown fox分数 = brown分数 + fox分数</code></li>
</ol>
<p>doc 1 分数 = 0.21110919 + 0 = 0.21110919</p>
<p>doc 2 分数 = 0.160443 + 0.60996956 = 0.77041256</p>
<p><img src="assets/es-dsl-dismax-8.png" alt="img" /></p>
<ol>
<li>所以整个语句分数， <code>should分数 = 第一个match + 第二个match分数</code></li>
</ol>
<p>doc 1 分数 = 0.6931471 + 0.21110919 = 0.90425634</p>
<p>doc 2 分数 = 0 + 0.77041256 = 0.77041256</p>
<p><img src="assets/es-dsl-dismax-9.png" alt="img" /></p>
<ul>
<li><strong>引入了dis_max</strong></li>
</ul>
<p>不使用 bool 查询，可以使用 dis_max 即分离 最大化查询（Disjunction Max Query） 。分离（Disjunction）的意思是 或（or） ，这与可以把结合（conjunction）理解成 与（and） 相对应。分离最大化查询（Disjunction Max Query）指的是： 将任何与任一查询匹配的文档作为结果返回，但只将最佳匹配的评分作为查询的评分结果返回 ：</p>
<pre><code class="language-bash">GET /test-dsl-dis-max/_search
{
    &quot;query&quot;: {
        &quot;dis_max&quot;: {
            &quot;queries&quot;: [
                { &quot;match&quot;: { &quot;title&quot;: &quot;Brown fox&quot; }},
                { &quot;match&quot;: { &quot;body&quot;:  &quot;Brown fox&quot; }}
            ],
            &quot;tie_breaker&quot;: 0
        }
    }
}
</code></pre>
<p><img src="assets/es-dsl-dismax-3.png" alt="img" /></p>
<p>0.77041256怎么来的呢？ 下文给你解释它如何计算出来的。</p>
<ul>
<li><strong>dis_max 条件的计算分数</strong></li>
</ul>
<p>分数 = 第一个匹配条件分数 + tie_breaker * 第二个匹配的条件的分数 ...</p>
<pre><code class="language-bash">GET /test-dsl-dis-max/_search
{
    &quot;query&quot;: {
        &quot;dis_max&quot;: {
            &quot;queries&quot;: [
                { &quot;match&quot;: { &quot;title&quot;: &quot;Brown fox&quot; }},
                { &quot;match&quot;: { &quot;body&quot;:  &quot;Brown fox&quot; }}
            ],
            &quot;tie_breaker&quot;: 0
        }
    }
}
</code></pre>
<p>doc 1 分数 = 0.6931471 + 0.21110919 * 0 = 0.6931471</p>
<p>doc 2 分数 = 0.77041256 = 0.77041256</p>
<p><img src="assets/es-dsl-dismax-10.png" alt="img" /></p>
<p>这样你就能理解通过dis_max将doc 2 置前了， 当然这里如果缺省<code>tie_breaker</code>字段的话默认就是0，你还可以设置它的比例（在0到1之间）来控制排名。（显然值为1时和should查询是一致的）</p>
<h2>function_score(函数查询）</h2>
<blockquote>
<p>简而言之就是用自定义function的方式来计算_score。</p>
</blockquote>
<p>可以ES有哪些自定义function呢？</p>
<ul>
<li><code>script_score</code> 使用自定义的脚本来完全控制分值计算逻辑。如果你需要以上预定义函数之外的功能，可以根据需要通过脚本进行实现。</li>
<li><code>weight</code> 对每份文档适用一个简单的提升，且该提升不会被归约：当weight为2时，结果为2 * _score。</li>
<li><code>random_score</code> 使用一致性随机分值计算来对每个用户采用不同的结果排序方式，对相同用户仍然使用相同的排序方式。</li>
<li><code>field_value_factor</code> 使用文档中某个字段的值来改变_score，比如将受欢迎程度或者投票数量考虑在内。</li>
<li><code>衰减函数(Decay Function)</code> - <code>linear</code>，<code>exp</code>，<code>gauss</code></li>
</ul>
<h3>例子</h3>
<p>以最简单的random_score 为例</p>
<pre><code class="language-bash">GET /_search
{
  &quot;query&quot;: {
    &quot;function_score&quot;: {
      &quot;query&quot;: { &quot;match_all&quot;: {} },
      &quot;boost&quot;: &quot;5&quot;,
      &quot;random_score&quot;: {}, 
      &quot;boost_mode&quot;: &quot;multiply&quot;
    }
  }
}
</code></pre>
<p>进一步的，它还可以使用上述function的组合(functions)</p>
<pre><code class="language-bash">GET /_search
{
  &quot;query&quot;: {
    &quot;function_score&quot;: {
      &quot;query&quot;: { &quot;match_all&quot;: {} },
      &quot;boost&quot;: &quot;5&quot;, 
      &quot;functions&quot;: [
        {
          &quot;filter&quot;: { &quot;match&quot;: { &quot;test&quot;: &quot;bar&quot; } },
          &quot;random_score&quot;: {}, 
          &quot;weight&quot;: 23
        },
        {
          &quot;filter&quot;: { &quot;match&quot;: { &quot;test&quot;: &quot;cat&quot; } },
          &quot;weight&quot;: 42
        }
      ],
      &quot;max_boost&quot;: 42,
      &quot;score_mode&quot;: &quot;max&quot;,
      &quot;boost_mode&quot;: &quot;multiply&quot;,
      &quot;min_score&quot;: 42
    }
  }
}
</code></pre>
<p>script_score 可以使用如下方式</p>
<pre><code class="language-bash">GET /_search
{
  &quot;query&quot;: {
    &quot;function_score&quot;: {
      &quot;query&quot;: {
        &quot;match&quot;: { &quot;message&quot;: &quot;elasticsearch&quot; }
      },
      &quot;script_score&quot;: {
        &quot;script&quot;: {
          &quot;source&quot;: &quot;Math.log(2 + doc['my-int'].value)&quot;
        }
      }
    }
  }
}
</code></pre>
<p>更多相关内容，可以参考<a href="https://www.elastic.co/guide/en/elasticsearch/reference/7.12/query-dsl-function-score-query.html">官方文档 </a>PS: 形成体系化认知以后，具体用的时候查询下即可。</p>
<h2>参考文章</h2>
<p>https://www.elastic.co/guide/en/elasticsearch/reference/current/compound-queries.html</p>
<p>https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-bool-query.html</p>
<p>https://www.elastic.co/guide/en/elasticsearch/reference/7.12/query-dsl-function-score-query.html</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="06&#32;索引：索引模板(Index&#32;Template)详解.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="08&#32;查询：DSL查询之全文搜索详解.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4340220fdf70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/ElasticSearch%E7%9F%A5%E8%AF%86%E4%BD%93%E7%B3%BB%E8%AF%A6%E8%A7%A3/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
