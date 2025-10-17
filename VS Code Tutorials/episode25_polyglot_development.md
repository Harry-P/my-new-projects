# Episode 25 — Advanced Language Features & Polyglot Development

## Mastering multi-language development
Modern projects often combine multiple programming languages and technologies. This episode covers advanced language features and strategies for polyglot development in VS Code.

## Language Server Protocol mastery

### Custom language server configuration
Advanced LSP settings for better performance:
```json
{
  "typescript.preferences.includePackageJsonAutoImports": "auto",
  "typescript.suggest.completeFunctionCalls": true,
  "typescript.inlayHints.parameterNames.enabled": "all",
  "typescript.inlayHints.variableTypes.enabled": true,
  "typescript.inlayHints.functionLikeReturnTypes.enabled": true,
  "python.analysis.autoImportCompletions": true,
  "python.analysis.typeCheckingMode": "strict",
  "python.analysis.inlayHints.functionReturnTypes": true,
  "rust-analyzer.inlayHints.parameterHints.enable": true,
  "rust-analyzer.inlayHints.typeHints.enable": true
}
```

### Language-specific workspace configurations
```json
{
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.organizeImports": true,
      "source.fixAll.eslint": true
    }
  },
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.organizeImports": true
    }
  },
  "[rust]": {
    "editor.defaultFormatter": "rust-lang.rust-analyzer",
    "editor.formatOnSave": true
  },
  "[go]": {
    "editor.defaultFormatter": "golang.go",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.organizeImports": true
    }
  }
}
```

## Advanced TypeScript development

### Complex type manipulations
```typescript
// Advanced utility types and generics
type DeepPartial<T> = {
  [P in keyof T]?: T[P] extends object ? DeepPartial<T[P]> : T[P];
};

type RequiredKeys<T> = {
  [K in keyof T]-?: {} extends Pick<T, K> ? never : K;
}[keyof T];

type OptionalKeys<T> = {
  [K in keyof T]-?: {} extends Pick<T, K> ? K : never;
}[keyof T];

// Advanced mapped types
type EventHandlers<T> = {
  [K in keyof T as `on${Capitalize<string & K>}`]: (event: T[K]) => void;
};

interface UserEvents {
  login: { userId: string; timestamp: Date };
  logout: { userId: string };
  purchase: { productId: string; amount: number };
}

type UserEventHandlers = EventHandlers<UserEvents>;
// Result: { onLogin: (event: {...}) => void; onLogout: ...; onPurchase: ... }
```

### Advanced debugging configurations
```json
{
  "name": "Debug TypeScript with Source Maps",
  "type": "node",
  "request": "launch",
  "program": "${workspaceFolder}/dist/index.js",
  "sourceMaps": true,
  "outFiles": ["${workspaceFolder}/dist/**/*.js"],
  "resolveSourceMapLocations": [
    "${workspaceFolder}/**",
    "!**/node_modules/**"
  ],
  "smartStep": true,
  "skipFiles": ["<node_internals>/**"]
}
```

## Python advanced features

### Type hints and static analysis
```python
from typing import TypeVar, Generic, Protocol, Literal, Union, overload
from dataclasses import dataclass
from abc import abstractmethod

T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')

class Comparable(Protocol):
    @abstractmethod
    def __lt__(self, other: 'Comparable') -> bool: ...

class Cache(Generic[K, V]):
    def __init__(self, max_size: int = 100) -> None:
        self._cache: dict[K, V] = {}
        self._max_size = max_size
    
    def get(self, key: K) -> V | None:
        return self._cache.get(key)
    
    def set(self, key: K, value: V) -> None:
        if len(self._cache) >= self._max_size:
            self._evict_oldest()
        self._cache[key] = value

@dataclass
class APIResponse(Generic[T]):
    success: bool
    data: T | None = None
    error: str | None = None
    
    @classmethod
    def success_response(cls, data: T) -> 'APIResponse[T]':
        return cls(success=True, data=data)
    
    @classmethod
    def error_response(cls, error: str) -> 'APIResponse[T]':
        return cls(success=False, error=error)
```

### Advanced debugging with breakpoints
```python
import logging
import sys
from typing import Any

def debug_decorator(func):
    """Advanced debugging decorator with conditional breakpoints"""
    def wrapper(*args, **kwargs):
        if logging.getLogger().isEnabledFor(logging.DEBUG):
            print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
            # Conditional breakpoint can be set here
            # breakpoint() if some_condition else None
        
        try:
            result = func(*args, **kwargs)
            if logging.getLogger().isEnabledFor(logging.DEBUG):
                print(f"{func.__name__} returned: {result}")
            return result
        except Exception as e:
            print(f"Exception in {func.__name__}: {e}")
            # Auto-breakpoint on exceptions
            if sys.gettrace() is not None:  # Check if debugger is attached
                breakpoint()
            raise
    
    return wrapper
```

## Rust development mastery

### Advanced Rust patterns
```rust
use std::marker::PhantomData;
use std::collections::HashMap;
use tokio::sync::RwLock;
use serde::{Serialize, Deserialize};

// Advanced trait bounds and associated types
trait Repository<T> {
    type Error;
    type Connection;
    
    async fn find_by_id(&self, id: u64) -> Result<Option<T>, Self::Error>;
    async fn save(&self, entity: &T) -> Result<T, Self::Error>;
    async fn delete(&self, id: u64) -> Result<(), Self::Error>;
}

// State machine with phantom types
struct Pending;
struct Validated;
struct Processed;

struct Order<State> {
    id: u64,
    items: Vec<String>,
    total: f64,
    _state: PhantomData<State>,
}

impl Order<Pending> {
    fn new(items: Vec<String>, total: f64) -> Self {
        Order {
            id: rand::random(),
            items,
            total,
            _state: PhantomData,
        }
    }
    
    fn validate(self) -> Result<Order<Validated>, String> {
        if self.total > 0.0 && !self.items.is_empty() {
            Ok(Order {
                id: self.id,
                items: self.items,
                total: self.total,
                _state: PhantomData,
            })
        } else {
            Err("Invalid order".to_string())
        }
    }
}

impl Order<Validated> {
    async fn process(self) -> Result<Order<Processed>, String> {
        // Process payment, update inventory, etc.
        tokio::time::sleep(tokio::time::Duration::from_millis(100)).await;
        
        Ok(Order {
            id: self.id,
            items: self.items,
            total: self.total,
            _state: PhantomData,
        })
    }
}
```

### Rust debugging configuration
```json
{
  "name": "Debug Rust Binary",
  "type": "lldb",
  "request": "launch",
  "program": "${workspaceFolder}/target/debug/${workspaceFolderBasename}",
  "args": [],
  "cwd": "${workspaceFolder}",
  "sourceLanguages": ["rust"],
  "terminal": "integrated"
}
```

## Go development advanced patterns

### Go generics and advanced patterns
```go
package main

import (
    "context"
    "fmt"
    "sync"
    "time"
)

// Generic constraint interface
type Ordered interface {
    ~int | ~int8 | ~int16 | ~int32 | ~int64 |
        ~uint | ~uint8 | ~uint16 | ~uint32 | ~uint64 | ~uintptr |
        ~float32 | ~float64 |
        ~string
}

// Generic data structures
type SafeMap[K comparable, V any] struct {
    mu sync.RWMutex
    m  map[K]V
}

func NewSafeMap[K comparable, V any]() *SafeMap[K, V] {
    return &SafeMap[K, V]{
        m: make(map[K]V),
    }
}

func (sm *SafeMap[K, V]) Set(key K, value V) {
    sm.mu.Lock()
    defer sm.mu.Unlock()
    sm.m[key] = value
}

func (sm *SafeMap[K, V]) Get(key K) (V, bool) {
    sm.mu.RLock()
    defer sm.mu.RUnlock()
    value, ok := sm.m[key]
    return value, ok
}

// Advanced worker pool pattern
type WorkerPool[T any, R any] struct {
    workers    int
    jobQueue   chan Job[T, R]
    resultChan chan Result[R]
    done       chan struct{}
    wg         sync.WaitGroup
}

type Job[T any, R any] struct {
    ID   string
    Data T
    Fn   func(T) (R, error)
}

type Result[R any] struct {
    ID     string
    Result R
    Error  error
}

func NewWorkerPool[T any, R any](workers int) *WorkerPool[T, R] {
    return &WorkerPool[T, R]{
        workers:    workers,
        jobQueue:   make(chan Job[T, R], workers*2),
        resultChan: make(chan Result[R], workers*2),
        done:       make(chan struct{}),
    }
}

func (wp *WorkerPool[T, R]) Start(ctx context.Context) {
    for i := 0; i < wp.workers; i++ {
        wp.wg.Add(1)
        go wp.worker(ctx)
    }
}

func (wp *WorkerPool[T, R]) worker(ctx context.Context) {
    defer wp.wg.Done()
    
    for {
        select {
        case job := <-wp.jobQueue:
            result, err := job.Fn(job.Data)
            wp.resultChan <- Result[R]{
                ID:     job.ID,
                Result: result,
                Error:  err,
            }
        case <-ctx.Done():
            return
        case <-wp.done:
            return
        }
    }
}
```

## Multi-language project organization

### Polyglot workspace structure
```
polyglot-project/
├── backend/
│   ├── rust-service/
│   │   ├── Cargo.toml
│   │   └── src/
│   ├── go-service/
│   │   ├── go.mod
│   │   └── main.go
│   └── python-service/
│       ├── pyproject.toml
│       └── src/
├── frontend/
│   ├── typescript-app/
│   │   ├── package.json
│   │   └── src/
│   └── wasm-module/
│       └── Cargo.toml
├── shared/
│   ├── proto/
│   └── types/
└── .vscode/
    ├── settings.json
    ├── tasks.json
    └── launch.json
```

### Multi-language tasks configuration
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Build All Services",
      "dependsOrder": "parallel",
      "dependsOn": [
        "Build Rust Service",
        "Build Go Service",
        "Build Python Service",
        "Build TypeScript App"
      ]
    },
    {
      "label": "Build Rust Service",
      "type": "shell",
      "command": "cargo",
      "args": ["build", "--release"],
      "options": {
        "cwd": "${workspaceFolder}/backend/rust-service"
      },
      "group": "build"
    },
    {
      "label": "Build Go Service", 
      "type": "shell",
      "command": "go",
      "args": ["build", "-o", "bin/service", "."],
      "options": {
        "cwd": "${workspaceFolder}/backend/go-service"
      },
      "group": "build"
    },
    {
      "label": "Build Python Service",
      "type": "shell",
      "command": "python",
      "args": ["-m", "build"],
      "options": {
        "cwd": "${workspaceFolder}/backend/python-service"
      },
      "group": "build"
    },
    {
      "label": "Test All",
      "dependsOrder": "parallel",
      "dependsOn": [
        "Test Rust",
        "Test Go", 
        "Test Python",
        "Test TypeScript"
      ]
    }
  ]
}
```

## Language interoperability

### WebAssembly integration
```rust
// Rust code compiled to WebAssembly
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub struct Calculator {
    value: f64,
}

#[wasm_bindgen]
impl Calculator {
    #[wasm_bindgen(constructor)]
    pub fn new() -> Calculator {
        Calculator { value: 0.0 }
    }
    
    #[wasm_bindgen]
    pub fn add(&mut self, value: f64) -> f64 {
        self.value += value;
        self.value
    }
    
    #[wasm_bindgen]
    pub fn multiply(&mut self, value: f64) -> f64 {
        self.value *= value;
        self.value
    }
    
    #[wasm_bindgen(getter)]
    pub fn value(&self) -> f64 {
        self.value
    }
}
```

```typescript
// TypeScript integration with WebAssembly
import init, { Calculator } from './pkg/calculator.js';

async function loadCalculator() {
  await init();
  const calc = new Calculator();
  
  calc.add(10);
  calc.multiply(2);
  
  console.log(`Result: ${calc.value}`); // Result: 20
}
```

### FFI (Foreign Function Interface)
```python
# Python calling Rust via FFI
import ctypes
from pathlib import Path

# Load the Rust library
lib_path = Path("target/release/libmylib.so")  # or .dll on Windows
lib = ctypes.CDLL(str(lib_path))

# Define function signatures
lib.process_data.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_size_t]
lib.process_data.restype = ctypes.c_double

def process_array(data: list[float]) -> float:
    """Process array using Rust implementation"""
    array_type = ctypes.c_double * len(data)
    c_array = array_type(*data)
    
    result = lib.process_data(c_array, len(data))
    return result
```

## Advanced debugging for polyglot projects

### Multi-language debugging session
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug Full Stack",
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}/frontend/src/index.ts",
      "runtimeArgs": ["--loader", "ts-node/esm"],
      "env": {
        "BACKEND_URL": "http://localhost:8080"
      }
    }
  ],
  "compounds": [
    {
      "name": "Debug Microservices",
      "configurations": [
        "Debug Rust Service",
        "Debug Go Service", 
        "Debug Python Service"
      ],
      "stopAll": true
    }
  ]
}
```

### Cross-language profiling
```bash
# Performance profiling across languages
#!/bin/bash

echo "Starting performance analysis..."

# Profile Rust service
cargo flamegraph --bin rust-service &
RUST_PID=$!

# Profile Go service  
go tool pprof -http=:8081 http://localhost:8080/debug/pprof/profile &
GO_PID=$!

# Profile Python service
py-spy record -o python-profile.svg -d 60 --pid $(pgrep -f python-service) &
PYTHON_PID=$!

# Run load test
artillery run load-test.yml

# Wait for profiling to complete
wait $RUST_PID $GO_PID $PYTHON_PID

echo "Profiling complete. Check generated reports."
```

## Performance optimization across languages

### Language-specific optimization strategies
```yaml
# Performance optimization checklist
optimization_strategies:
  rust:
    - Use release builds with LTO
    - Profile with flamegraph and perf
    - Optimize allocations with custom allocators
    - Use async/await for I/O bound operations
    
  go:
    - Use pprof for CPU and memory profiling
    - Optimize garbage collection settings
    - Use sync.Pool for object reuse
    - Profile with go tool trace
    
  python:
    - Use Cython for CPU-intensive code
    - Profile with py-spy and cProfile
    - Use asyncio for I/O bound operations
    - Consider PyPy for compute-heavy workloads
    
  typescript:
    - Use webpack bundle analyzer
    - Implement code splitting
    - Optimize with tree shaking
    - Use service workers for caching
```

### Cross-language benchmarking
```python
# Unified benchmarking across languages
import subprocess
import time
import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class BenchmarkResult:
    language: str
    operation: str
    duration_ms: float
    memory_mb: float
    
class PolyglotBenchmark:
    def __init__(self):
        self.results: List[BenchmarkResult] = []
    
    def run_rust_benchmark(self, operation: str) -> BenchmarkResult:
        start_time = time.perf_counter()
        result = subprocess.run([
            "cargo", "run", "--release", "--bin", "benchmark", 
            "--", operation
        ], capture_output=True, text=True, cwd="backend/rust-service")
        end_time = time.perf_counter()
        
        return BenchmarkResult(
            language="rust",
            operation=operation,
            duration_ms=(end_time - start_time) * 1000,
            memory_mb=self._get_memory_usage(result.stdout)
        )
    
    def run_all_benchmarks(self) -> Dict[str, List[BenchmarkResult]]:
        operations = ["fibonacci", "matrix_multiply", "json_parse"]
        
        for operation in operations:
            self.results.append(self.run_rust_benchmark(operation))
            self.results.append(self.run_go_benchmark(operation))
            self.results.append(self.run_python_benchmark(operation))
        
        return self._group_results_by_operation()
```

Polyglot development is the future—master these advanced language features to build sophisticated, multi-technology solutions that leverage the best of each language!