package main

import (
	"testing"
)

func TestNewFoo(t *testing.T) {
	result := newFoo()
	if result != nil {
		t.Errorf("expecting foo, got %s", result)
	}

}
