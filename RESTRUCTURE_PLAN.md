# 文件结构重构计划

## 当前结构 → 新结构映射

### 推荐的新文件结构:

```
notebooks/
├── README.md                              # 项目总览和使用指南
├── ai-machine-learning/                   # AI和机器学习相关内容
│   ├── README.md                          # AI/ML模块总览
│   ├── deep-learning-specialization/      # 深度学习专精
│   │   ├── README.md
│   │   ├── notes/
│   │   │   └── deeplearning-specialization.md
│   │   ├── assignments/
│   │   │   ├── course1/
│   │   │   ├── course2/
│   │   │   ├── course3/
│   │   │   ├── course4/
│   │   │   └── course5/
│   │   └── images/
│   ├── tensorflow-developer/              # TensorFlow开发者
│   │   ├── README.md
│   │   ├── notes/
│   │   │   └── tensorflow-developer.md
│   │   ├── assignments/
│   │   └── images/
│   ├── ml-ops-specialization/             # ML运营专精
│   │   ├── README.md
│   │   ├── notes/
│   │   │   └── ml-ops-specialization.md
│   │   ├── assignments/
│   │   └── images/
│   └── shared-resources/                  # AI/ML共享资源
├── business-entrepreneurship/             # 商业和创业
│   ├── README.md
│   ├── notes/
│   │   ├── english-for-business.md
│   │   └── relationship-management.md
│   └── materials/
├── project-management/                    # 项目管理
│   ├── README.md
│   ├── notes/
│   │   └── google-pmp-certification.md
│   ├── materials/
│   └── images/
└── resources/                             # 全局资源
    ├── templates/                         # 模板文件
    └── shared-materials/                  # 共享材料
```

## 文件迁移映射

### 当前 → 新位置:

1. **AI文件夹内容**:
   - `AI/2402_deeplearning_specialization.md` → `ai-machine-learning/deep-learning-specialization/notes/deeplearning-specialization.md`
   - `AI/2401_deeplearning_developer.md` → `ai-machine-learning/tensorflow-developer/notes/tensorflow-developer.md`
   - `AI/2404_ml_ops_specialization.md` → `ai-machine-learning/ml-ops-specialization/notes/ml-ops-specialization.md`

2. **作业文件**:
   - `AI/assignments/deeplearning_specialization/` → `ai-machine-learning/deep-learning-specialization/assignments/`
   - `AI/assignments/tensorflow_developer/` → `ai-machine-learning/tensorflow-developer/assignments/`
   - `AI/assignments/ml_operation_specialization/` → `ai-machine-learning/ml-ops-specialization/assignments/`

3. **图片文件**:
   - `AI/images/2402_deeplearning_specialization/` → `ai-machine-learning/deep-learning-specialization/images/`
   - `AI/images/2401_deeplearning_developer/` → `ai-machine-learning/tensorflow-developer/images/`
   - `AI/images/2404_ml_ops_specialization/` → `ai-machine-learning/ml-ops-specialization/images/`

4. **商业文件**:
   - `business/English for Business and Entrepreneurship.md` → `business-entrepreneurship/notes/english-for-business.md`
   - `business/Others.md` → `business-entrepreneurship/notes/relationship-management.md`

5. **项目管理文件**:
   - `pmp/2408_google_pmp.md` → `project-management/notes/google-pmp-certification.md`
   - `pmp/materials/` → `project-management/materials/`
   - `pmp/image-*.png` → `project-management/images/`

6. **学习材料**:
   - `materials/` → `resources/shared-materials/`

## 新结构的优势

1. **清晰的分类**：按学习领域分组，便于查找和管理
2. **一致的结构**：每个模块都有notes、assignments、images等统一结构
3. **GitHub友好**：使用kebab-case命名，符合GitHub项目惯例
4. **扩展性强**：容易添加新的课程或专精
5. **版本控制友好**：文件组织便于Git管理和协作
6. **文档完整**：每个文件夹都有README说明

## 实施步骤

1. 创建新的目录结构
2. 迁移和重命名文件
3. 更新文件内的图片路径引用
4. 创建各级README文档
5. 清理旧的文件结构
6. 添加.gitignore文件

这个结构将使您的notebooks项目更加专业和易于维护！ 